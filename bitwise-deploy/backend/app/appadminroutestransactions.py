from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models import Transaction, Client
from app.utils.audit import log_audit
from datetime import datetime

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('', methods=['GET'])
@jwt_required()
def get_transactions():
    page, limit = request.args.get('page',1,type=int), request.args.get('limit',10,type=int)
    q = Transaction.query
    for f in ['type','status','client_id']:
        if request.args.get(f): q = q.filter_by(**{f:request.args.get(f)})
    pag = q.order_by(Transaction.created_at.desc()).paginate(page=page, per_page=limit, error_out=False)
    txs = [{'id':t.id,'client_id':t.client_id,'type':t.type,'amount':t.amount,'currency':t.currency,'status':t.status,'description':t.description,'recipient_name':t.recipient_name,'recipient_iban':t.recipient_iban,'blocked_reason':t.blocked_reason,'created_at':t.created_at.isoformat()} for t in pag.items]
    return jsonify({'transactions':txs,'total':pag.total,'pages':pag.pages,'current_page':page}), 200

@transactions_bp.route('', methods=['POST'])
@jwt_required()
def create_transaction():
    data = request.get_json()
    if not Client.query.get(data.get('client_id')): return jsonify({'error':'Client not found'}), 404
    t = Transaction(client_id=data['client_id'],type=data['type'],amount=data['amount'],currency=data.get('currency','EUR'),description=data.get('description',''),recipient_name=data.get('recipient_name'),recipient_iban=data.get('recipient_iban'),recipient_bic=data.get('recipient_bic'))
    db.session.add(t); db.session.commit()
    log_audit('transaction_create', f"Tx #{t.id} created", 'low')
    return jsonify({'message':'Created','transaction_id':t.id}), 201

@transactions_bp.route('/<tx_id>/<action>', methods=['POST'])
@jwt_required()
def manage_transaction(tx_id, action):
    t = Transaction.query.get(tx_id)
    if not t: return jsonify({'error':'Not found'}), 404
    data = request.get_json() or {}
    rules = {
        'block': (t.status=='pending', lambda: setattr(t,'status','blocked') or setattr(t,'blocked_reason',data.get('reason','Blocked'))),
        'unblock': (t.status=='blocked', lambda: setattr(t,'status','pending') or setattr(t,'blocked_reason',None)),
        'execute': (t.status in ['pending','blocked'], lambda: setattr(t,'status','completed') or setattr(t,'executed_at',datetime.utcnow())),
        'cancel': (t.status not in ['completed','cancelled'], lambda: setattr(t,'status','cancelled'))
    }
    if action not in rules: return jsonify({'error':'Invalid action'}), 400
    ok, fn = rules[action]
    if not ok: return jsonify({'error':'Invalid status for action'}), 400
    fn(); t.updated_at = datetime.utcnow()
    db.session.commit()
    log_audit(f'transaction_{action}', f"Tx #{t.id} {action}ed", 'high' if action=='block' else 'medium')
    return jsonify({'message':f'{action.capitalize()}ed'}), 200