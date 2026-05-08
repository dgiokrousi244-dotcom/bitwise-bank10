from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import AuditLog

audit_bp = Blueprint('audit', __name__)

@audit_bp.route('', methods=['GET'])
@jwt_required()
def get_audit_logs():
    page, limit, severity = request.args.get('page',1,type=int), request.args.get('limit',50,type=int), request.args.get('severity')
    q = AuditLog.query
    if severity: q = q.filter_by(severity=severity)
    pag = q.order_by(AuditLog.timestamp.desc()).paginate(page=page, per_page=limit, error_out=False)
    logs = [{'id':l.id,'timestamp':l.timestamp.isoformat(),'action':l.action,'user_email':l.user_email,'details':l.details,'severity':l.severity,'ip_address':l.ip_address} for l in pag.items]
    return jsonify({'logs':logs,'total':pag.total,'pages':pag.pages,'current_page':page}), 200