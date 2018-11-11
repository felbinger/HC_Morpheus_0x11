from flask import Flask, render_template, redirect, url_for, jsonify, request, flash
from .config import Config
from .db import db
from .models import Token
from datetime import datetime


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    register_views(app)
    return app


def register_views(app: Flask):
    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            if request.form is not None:
                token = request.form.get('token')
                if token:
                    obj = Token.query.filter_by(token=token).first()
                    if obj:
                        if datetime.now() < obj.expires:
                            db.session.delete(obj)
                            db.session.commit()
                            flash('TMT{y32kTNmdLlBbm4rS1Ysx}', 'success')
                        else:
                            db.session.delete(obj)
                            db.session.commit()
                            flash('Too late', 'danger')
                    else:
                        flash('Invalid Token!', 'danger')
        return render_template('login.html'), 200

    @app.route('/generateLoginToken', methods=['POST'])
    def generate_token():
        token = Token()
        db.session.add(token)
        db.session.commit()
        return jsonify(token.jsonify()), 200
