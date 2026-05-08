from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models import ValidationCode
from app.utils.audit import log_audit
from datetime import datetime, timedelta
import random, string

codes_bp = Blueprint('codes', __name__)

@codes_bp.route('', methods=['GET'])
@jwt_required()
def get_codes():
    page, limit = request.args.get('page',1,type=int), request.args.get('limit',15,type=int)
    pag = ValidationCode.query.order_by(ValidationCode.created_at.desc()).paginate(page=page, per_page=limit, error_out=False)
    items = [{'id':c.id,'code':c.code,'code_type':c.code_type,'recipient':c.recipient,'is_used':c.is_used,'is_valid':c.is_valid,'attempts':c.attempts,'max_attempts':c.max_attempts,'expires_at':c.expires_at.isoformat(),'created_at':c.created_at.isoformat()} for c in pag.items]
    return jsonify({'codes':items,'total':pag.total,'pages':pag.pages,'current_page':page}), 200

@codes_bp.route('/generate', methods=['POST'])
@jwt_required()
def generate_code():
    data = request.get_json()
    if not data.get('code_type') or not data.get('recipient'): return jsonify({'error':'Missing fields'}), 400
    code_val = ''.join(random.choices(string.digits, k=6))
    while ValidationCode.query.filter_by(code=code_val).first(): code_val = ''.join(random.choices(string.digits, k=6))
    expires = datetime.utcnow() + timedelta(minutes=data.get('expiration_minutes',15))
    vc = ValidationCode(code=code_val,code_type=data['code_type'],recipient=data['recipient'],expires_at=expires,max_attempts=data.get('max_attempts',3))
    db.session.add(vc); db.session.commit()
    log_audit('code_generate', f"Code generated for {vc.recipient}", 'low')
    return jsonify({'message':'Generated','code_id':vc.id,'code':vc.code,'expires_at':expires.isoformat()}), 201

@codes_bp.route('/<code_id>/verify', methods=['POST'])
@jwt_required()
def verify_code(code_id):
    vc = ValidationCode.query.get(code_id)
    if not vc or not vc.is_valid: return jsonify({'error':'Invalid'}), 400
    if vc.code != request.get_json().get('code'):
        vc.attempts += 1; db.session.commit()
        return jsonify({'error':'Incorrect','attempts_remaining':vc.max_attempts-vc.attempts}), 401
    vc.is_used=True; vc.is_valid=False; db.session.commit()
    return jsonify({'message':'Verified'}), 200