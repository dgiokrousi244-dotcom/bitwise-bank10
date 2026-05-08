from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models import Client

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/operations/dashboard', methods=['GET'])
@jwt_required()
def get_stats():
    total = Client.query.count()
    active = Client.query.filter_by(account_status='active').count()
    balance = db.session.query(db.func.sum(Client.available_balance)).scalar() or 0.0
    return jsonify({'total_clients':total,'active_clients':active,'total_balance':balance,'timestamp':db.func.now()}), 200