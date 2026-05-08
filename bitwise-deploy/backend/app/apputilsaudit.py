from flask import request
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from app.extensions import db
from app.models import AuditLog, Admin
from datetime import datetime

def log_audit(action, details, severity='medium'):
    try:
        email = 'system'
        try:
            verify_jwt_in_request(optional=True)
            admin_id = get_jwt_identity()
            if admin_id:
                admin = Admin.query.get(admin_id)
                email = admin.email if admin else email
        except: pass

        entry = AuditLog(
            timestamp=datetime.utcnow(), action=action, user_email=email,
            details=details, severity=severity, ip_address=request.remote_addr
        )
        db.session.add(entry)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"[AUDIT ERROR] {e}")