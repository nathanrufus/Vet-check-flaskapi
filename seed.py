from faker import Faker
from app import create_app
from app.models.owner_model import Owner
from app import db

app = create_app()

fake=Faker()

owners =[]
def create_owners():
    for _ in range(15):
        email=fake.email()
        username=fake.name()
        owners.append(Owner(email=email,username=username))
    db.session.add_all(owners)
    db.commit()    


