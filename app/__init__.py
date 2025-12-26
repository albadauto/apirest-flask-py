from flask import Flask
from .config import Config
from .extensions import db, jwt
from .routes import user_bp, products_bp, login_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(user_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(login_bp)
    
    
    with app.app_context():
        db.create_all()
        
    return app