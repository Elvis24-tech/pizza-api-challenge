from flask import Flask

def create_app():
    app = Flask(__name__)
    from server.controllers.restaurant_controller import restaurants_bp
    from server.controllers.pizza_controller import pizzas_bp
    from server.controllers.restaurant_pizza_controller import restaurant_pizzas_bp
    app.register_blueprint(restaurants_bp)
    app.register_blueprint(pizzas_bp)
    app.register_blueprint(restaurant_pizzas_bp)
    return app