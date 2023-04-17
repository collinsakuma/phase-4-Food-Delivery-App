from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

from config import db

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-created_at', '-updated_at', '-orders', '-items')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    address = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    upated_at = db.Column(db.DateTime, onupdate=db.func.now())

    orders = db.relationship('Order', backref='user')
    items = association_proxy('orders', 'item')

class Item(db.Model, SerializerMixin):
    __tablename__ = 'items'

    serialize_rules = ('-created_at', '-updated_at', '-orders', '-users')

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    catgory = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    upated_at = db.Column(db.DateTime, onupdate=db.func.now())

    orders = db.relationship('Order', backref='item')
    users = association_proxy('orders', 'user')

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    serialize_rules = ('-created_at', '-updated_at', '-users', '-items')

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    upated_at = db.Column(db.DateTime, onupdate=db.func.now())

