from datetime import datetime
from utils.db import db
from sqlalchemy_serializer import SerializerMixin

class Product(db.Model, SerializerMixin):
    '''
        Product Model 
    '''

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.utcnow)
