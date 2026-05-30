import os
from flask import Flask, render_template
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

# These imports must match your folder and variable names exactly
from config import Config
from database.db import db
from auth.auth_routes import auth_bp
from files.file_routes import file_bp
from attack_simulation.attack_routes import attack_bp
from logs.log_routes import log_bp

def create_app():
    app = Flask(
        __name__,
        template_folder='../frontend/templates',
        static_folder='../frontend/static'
    )
    
    # 1. Load Configuration
    app.config.from_object(Config)
    
    # 2. Initialize Extensions
    CORS(app)
    db.init_app(app)
    JWTManager(app)
    Bcrypt(app)

    # 3. Register Blueprints (The "Links" to your folders)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(file_bp, url_prefix='/files')
    app.register_blueprint(attack_bp, url_prefix='/attacks')
    app.register_blueprint(log_bp, url_prefix='/logs')

    # 4. Create Tables Automatically
    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return render_template('login.html')

    @app.route('/login.html')
    def login_page():
        return render_template('login.html')

    @app.route('/register.html')
    def register_page():
        return render_template('register.html')

    @app.route('/dashboard.html')
    def dashboard_page():
        return render_template('dashboard.html')

    @app.route('/upload.html')
    def upload_page():
        return render_template('upload.html')

    @app.route('/files.html')
    def files_page():
        return render_template('files.html')

    @app.route('/attack.html')
    def attack_page():
        return render_template('attack.html')

    @app.route('/logs.html')
    def logs_page():
        return render_template('logs.html')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))

