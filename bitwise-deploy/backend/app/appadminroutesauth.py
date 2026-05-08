from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app.extensions import db
from app.models import Admin
from app.utils.audit import log_audit

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing email or password'}), 400
    if Admin.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 409
    admin = Admin(email=data['email'], full_name=data.get('full_name',''), role=data.get('role','admin'))
    admin.set_password(data['password'])
    db.session.add(admin); db.session.commit()
    log_audit('admin_register', f"New admin: {admin.email}", 'high')
    return jsonify({'message': 'Admin registered', 'admin_id': admin.id}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing credentials'}), 400
    admin = Admin.query.filter_by(email=data['email']).first()
    if not admin or not admin.check_password(data['password']) or not admin.is_active:
        return jsonify({'error': 'Invalid credentials or inactive account'}), 401
    access = create_access_token(identity=admin.id)
    refresh = create_refresh_token(identity=admin.id)
    log_audit('login_success', f"Admin login: {admin.email}", 'low')
    return jsonify({'access_token': access, 'refresh_token': refresh, 'admin_id': admin.id, 'email': admin.email, 'full_name': admin.full_name}), 200

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    return jsonify({'access_token': create_access_token(identity=get_jwt_identity())}), 200

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_profile():
    admin = Admin.query.get(get_jwt_identity())
    if not admin: return jsonify({'error': 'Not found'}), 404
    return jsonify({'id': admin.id, 'email': admin.email, 'full_name': admin.full_name, 'role': admin.role, 'is_active': admin.is_active, 'created_at': admin.created_at.isoformat()}), 200