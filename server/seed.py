#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
# from faker import Faker

# Local imports
from app import app
from models import db, User, Item, Order
#path to postgresql in zschrc
# echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc

if __name__ == '__main__':
    #fake = Faker()
    with app.app_context():
        print("Deleting records...")
        Item.query.delete()

        print("Creating Items...")

        item_1 = Item(
            name = "Mac n Cheese",
            price = 10,
            category = "pasta",
            img_url = "someimage"
        )

        item_2 = Item(
            name= 'Hamburger',
            price = 8,
            category = 'American',
            img_url = 'aburger'
            
        )
        
        # Seed code goes here!
        db.session.add_all([item_1, item_2])
        db.session.commit()

        print("db seeded")