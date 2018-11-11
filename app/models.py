from sqlalchemy import Column, String, DateTime, Integer
from datetime import datetime, timedelta
from random import SystemRandom
from string import ascii_letters, digits, punctuation
from flask import current_app

from app.db import db


class Token(db.Model):
    id = Column('id', Integer, primary_key=True)
    token = Column('token', String(128), unique=True, nullable=False)
    created = Column('created', DateTime, nullable=False)
    expires = Column('expires', DateTime, nullable=False)

    def __init__(self):
        expires = datetime.now() + timedelta(seconds=current_app.config['TOKEN_VALIDITY'])
        token = ''.join(SystemRandom().choice(ascii_letters + digits + punctuation) for _ in range(128))
        super().__init__(token=token, created=datetime.utcnow(), expires=expires)

    def jsonify(self) -> dict:
        return {
            'token': self.token,
            'expires': self.expires.utcnow().isoformat()
        }
