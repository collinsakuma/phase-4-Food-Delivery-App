#!/usr/bin/env python3

# Standard library imports
# Remote library imports
from flask import request, session, jsonify, make_response
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

# Local imports
from config import *
from models import db, User, Item, Order



# Views go here!
class Items(Resource):

    def get(self):
        items = [item.to_dict() for item in Item.query.all()]
        return make_response(items, 200)
api.add_resource(Items, '/items')

class Users(Resource):

    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(users, 200)
api.add_resource(Users, '/users')


class Orders(Resource):
    
    def get(self):
        orders = [order.to_dict() for order in Order.query.all()]
        return make_response(orders, 200)
api.add_resource(Orders, '/orders')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
