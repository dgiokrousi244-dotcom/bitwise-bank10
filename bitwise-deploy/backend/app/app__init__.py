import os
from flask import Flask
from flask_cors import CORS
from app.config import config
from app.extensions import db, jwt, cors, limiter

def create_app(config_name=None):
    app = Flask(__name__)
    cfg = config.get(config_name or 'development')
    app.config.from_object(cfg)

    origins = [o.strip() for o in os.getenv('CORS_ORIGINS', 'http://localhost:8000').split(',') if o.strip()]
    cors.init_app(app, resources={r"/api/*": {"origins": origins, "methods": ["GET","POST","PUT","DELETE","OPTIONS","PATCH"], "supports_credentials": True}})
    limiter.init_app(app)
    db.init_app(app)
    jwt.init_app(app)

    from app.admin.routes.auth import auth_bp
    from app.admin.routes.clients import clients_bp
    from app.admin.routes.transactions import transactions_bp
    from app.admin.routes.credits import credits_bp
    from app.admin.routes.codes import codes_bp
    from app.admin.routes.audit import audit_bp
    from app.admin.routes.dashboard import dashboard_bp

    prefix = '/api/admin'
    app.register_blueprint(auth_bp, url_prefix=f'{prefix}/auth')
    app.register_blueprint(clients_bp, url_prefix=f'{prefix}/clients')
    app.register_blueprint(transactions_bp, url_prefix=f'{prefix}/transactions')
    app.register_blueprint(credits_bp, url_prefix=f'{prefix}/credits')
    app.register_blueprint(codes_bp, url_prefix=f'{prefix}/codes')
    app.register_blueprint(audit_bp, url_prefix=f'{prefix}/audit')
    app.register_blueprint(dashboard_bp, url_prefix=prefix)

    @app.cli.command("init-db")
    def init_db():
        db.create_all()
        print("✅ Database tables created.")

    return app