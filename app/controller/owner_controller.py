from flask import request, jsonify
from app.models.owner_model import Owner
from app import db
from sqlalchemy.exc import SQLAlchemyError
import logging

logging.basicConfig(level=logging.INFO)

def handle_error(e, status_code):
    logging.error(str(e))
    return jsonify({'error' : str(e)}), status_code
def create_owner():
    try:
        data = request.get_json()

        if 'email' not in data or 'username' not in data :
            return handle_error('Missing data fields (username, email, date_processed required)', 400)
        
        new_owner = Owner(username=data['username'], email=data['email'])
        db.session.add(new_owner)
        db.session.commit()
        logging.info(jsonify(new_owner.serialize()))
        return jsonify(new_owner.serialize()), 201
    
    except SQLAlchemyError as e:
        return handle_error(e, 500)

def get_owners():
    try:
        owners=Owner.query.all()
        return jsonify([owner.serialize() for owner in owners])      
    except SQLAlchemyError as e :
        return handle_error(e,500)
    
def get_owner(id):
    try:
        owner=Owner.query.filter(id==id).first()
        return jsonify(owner.serialize())
    except SQLAlchemyError as e:
        return handle_error(e,500)
def update_owner(id):
    try:
        owner=Owner.query.filter(id==id).first()
        data=request.get_json()
        for attr in data:
            setattr(owner,attr,data(attr))
        db.session.commit()    
        return jsonify(owner.serialize())
    except SQLAlchemyError as e:
        return handle_error(e,500)
    
def delete_owner(id):
    try:
        owner=Owner.query.filter(id==id).first()
        db.session.delete(owner)
        db.session.commit()
        return jsonify(owner.serialize())
    except SQLAlchemyError as e:
        return handle_error(e,500)

  