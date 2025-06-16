from flask import Flask
from server.config import app, db
from server.controllers import restaurant_controller, pizza_controller, restaurant_pizza_controller

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)