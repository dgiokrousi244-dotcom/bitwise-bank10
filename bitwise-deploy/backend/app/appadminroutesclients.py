from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models import Client
from app.utils.audit import log_audit
from datetime import datetime

clients_bp = Blueprint('clients', __name__)

@clients_bp.route('', methods=['GET'])
@jwt_required()
def get_clients():
    page, limit, search = request.args.get('page',1,type=int), request.args.get('limit',10,type=int), request.args.get('search','',type=str)
    q = Client.query
    if search: q = q.filter((Client.full_name.ilike(f'%{search}%')) | (Client.email.ilike(f'%{search}%')))
    pag = q.order_by(Client.created_at.desc()).paginate(page=page, per_page=limit, error_out=False)
    return jsonify({'clients': [{'id':c.id,'full_name':c.full_name,'email':c.email,'phone':c.phone,'iban':c.iban,'available_balance':c.available_balance,'kyc_status':c.kyc_status,'account_status':c.account_status,'created_at':c.created_at.isoformat()} for c in pag.items], 'total':pag.total,'pages':pag.pages,'current_page':page}), 200

@clients_bp.route('/<client_id>', methods=['GET'])
@jwt_required()
def get_client(client_id):
    c = Client.query.get(client_id)
    if not c: return jsonify({'error':'Not found'}), 404
    return jsonify({'id':c.id,'full_name':c.full_name,'email':c.email,'phone':c.phone,'iban':c.iban,'bic_swift':c.bic_swift,'available_balance':c.available_balance,'kyc_status':c.kyc_status,'account_status':c.account_status,'created_at':c.created_at.isoformat(),'updated_at':c.updated_at.isoformat()}), 200

@clients_bp.route('/<client_id>', methods=['PUT'])
@jwt_required()
def update_client(client_id):
    c = Client.query.get(client_id)
    if not c: return jsonify({'error':'Not found'}), 404
    data = request.get_json()
    for k in ['full_name','phone','iban','bic_swift','available_balance','kyc_status','account_status']:
        if k in data: setattr(c, k, data[k])
    c.updated_at = datetime.utcnow()
    db.session.commit()
    log_audit('client_update', f"Updated client #{c.id}", 'medium')
    return jsonify({'message':'Updated'}), 200

@clients_bp.route('/<client_id>/suspend', methods=['POST'])
@clients_bp.route('/<client_id>/activate', methods=['POST'])
@jwt_required()
def toggle_status(client_id):
    c = Client.query.get(client_id)
    if not c: return jsonify({'error':'Not found'}), 404
    action = 'suspend' if 'suspend' in request.url_rule.rule else 'activate'
    c.account_status = 'suspended' if action == 'suspend' else 'active'
    c.updated_at = datetime.utcnow()
    db.session.commit()
    log_audit(f'client_{action}', f"Client #{c.id} {action}ed", 'high')
    return jsonify({'message':f'Client {action}ed'}), 200