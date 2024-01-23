from app import db
from datetime import datetime


class Owner(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email =db.Column(db.String(100),nullable=False,unique=True)
    username =db.Column(db.String(100),nullable=False)
    date_processed =db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
    
    #pets =db.relationship('Pet',backref='owner', lazy=True)
     
    def __rep__(self):
        return f'<Pet Owner {self.name}>'
     
    def serialize(self):
        return{
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'date_processed': self.date_processed
        }