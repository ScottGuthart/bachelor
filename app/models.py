from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Sortable(db.Model):
    __tablename__ = 'sortables'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.String)

    def __init__(self, data):
        self.data = data