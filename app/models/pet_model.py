from app import db


class Pet(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    species =db.Column(db.String(100),nullable=False)
    name =db.Column(db.String(100),nullable=False)
    pet =db.relationship('Owner')
    owner_id = db.Column(db.Integer,db.Foreignkey('owners.id'))

    def __rep__(self):
        return f'<Pet  {self.name}>'
    def serialize(self):
        return {
            'id':self.id,
            'species':self.species,
            'name':self.name,
            'owner_details':self.pet.serialize() if self.owner else None
        }