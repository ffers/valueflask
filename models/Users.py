from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db import db
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Posts', backref='users', passive_deletes=True)
    comments = db.relationship('Comment', backref='users', passive_deletes=True)
    likes = db.relationship('Likes', backref='users', passive_deletes=True)