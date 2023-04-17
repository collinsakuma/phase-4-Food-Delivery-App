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
class Item_things(Resource):

    def get(self):
        items = [item.to_dict() for item in Item.query.all()]
        return make_response(items, 200)
api.add_resource(Item_things, '/api/items')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
