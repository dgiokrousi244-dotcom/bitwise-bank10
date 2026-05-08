from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models import CreditRequest, Client
from app.utils.audit import log_audit
from datetime import datetime

credits_bp = Blueprint('credits', __name__)

@credits_bp.route('', methods=['GET'])
@jwt_required()
def get_credits():
    page, limit, status = request.args.get('page',1,type=int), request.args.get('limit',10,type=int), request.args.get('status')
    q = CreditRequest.query
    if status: q = q.filter_by(status=status)
    pag = q.order_by(CreditRequest.created_at.desc()).paginate(page=page, per_page=limit, error_out=False)
    items = [{'id':cr.id,'client_id':cr.client_id,'amount':cr.amount,'currency':cr.currency,'purpose':cr.purpose,'status':cr.status,'created_at':cr.created_at.isoformat()} for cr in pag.items]
    return jsonify({'credits':items,'total':pag.total,'pages':pag.pages,'current_page':page}), 200

@credits_bp.route('', methods=['POST'])
def create_credit():
    data = request.get_json()
    if not Client.query.get(data.get('client_id')): return jsonify({'error':'Client not found'}), 404
    cr = CreditRequest(client_id=data['client_id'],amount=data['amount'],currency=data.get('currency','EUR'),purpose=data.get('purpose',''))
    db.session.add(cr); db.session.commit()
    return jsonify({'message':'Credit requested','id':cr.id}), 201

@credits_bp.route('/<cr_id>/review', methods=['POST'])
@jwt_required()
def review_credit(cr_id):
    cr = CreditRequest.query.get(cr_id)
    if not cr: return jsonify({'error':'Not found'}), 404
    if cr.status != 'pending': return jsonify({'error':'Already reviewed'}), 400
    data = request.get_json()
    if data.get('decision') not in ['approved','rejected']: return jsonify({'error':'Invalid decision'}), 400
    cr.status = data['decision']; cr.review_notes = data.get('notes',''); cr.reviewed_at = datetime.utcnow()
    db.session.commit()
    log_audit(f'credit_{cr.status}', f"Credit #{cr.id} {cr.status}", 'high')
    return jsonify({'message':f'Credit {cr.status}'}), 200