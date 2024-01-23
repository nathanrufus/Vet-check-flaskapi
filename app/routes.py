from flask import Blueprint
from app.controller.owner_controller import create_owner,get_owners,get_owner,update_owner,delete_owner

bp= Blueprint('bp',__name__)

@bp.route('/')
def home():
    return '<h1>Home route</h1>'

@bp.route('/owners',methods=['POST'])
def add_owner():
    return create_owner()

@bp.route ('/owners', methods=['GET'])
def list_owners():
    return get_owners()

@bp.route('/owners/<int:id>', methods=['GET'])
def list_owner(id):
    return get_owner(id)

@bp.route('/owners/<int:id>', methods=['PATCH'])
def change_owner(id):
    return update_owner(id)

@bp.route('/owners/<int:id>', methods=['DELETE'])
def remove_owner(id):
    return delete_owner(id)