Pizza Restaurant API
This is a RESTful API for a Pizza Restaurant built using Flask, following the MVC pattern. It manages Restaurants, Pizzas, and RestaurantPizzas with appropriate validations and relationships.
Setup Instructions

Create and Activate Virtual Environment:
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell


Set Flask Environment Variable:
export FLASK_APP=server/app.py


Initialize Database:
flask db init
flask db migrate -m "Initial migration"
flask db upgrade


Seed Database:
python server/seed.py



Database Migration & Seeding

Migrations: Managed using Flask-Migrate. Run flask db migrate to create migrations and flask db upgrade to apply them.
Seeding: The seed.py file populates the database with sample data for Restaurants, Pizzas, and RestaurantPizzas. Run python server/seed.py to seed.

Route Summary



Method
Endpoint
Description



GET
/restaurants
List all restaurants


GET
/restaurants/<int:id>
Get details of a restaurant and its pizzas


DELETE
/restaurants/<int:id>
Delete a restaurant and its RestaurantPizzas


GET
/pizzas
List all pizzas


POST
/restaurant_pizzas
Create a new RestaurantPizza


Example Requests & Responses
GET /restaurants
Response (200):
[
  {
    "id": 1,
    "name": "Dominos",
    "address": "123 Main St"
  },
  ...
]

GET /restaurants/int:id
Success Response (200):
{
  "id": 1,
  "name": "Dominos",
  "address": "123 Main St",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    ...
  ]
}

Error Response (404):
{ "error": "Restaurant not found" }

DELETE /restaurants/int:id
Success Response (204): No content Error Response (404):
{ "error": "Restaurant not found" }

GET /pizzas
Response (200):
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  ...
]

POST /restaurant_pizzas
Request:
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}

Success Response (201):
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 3,
    "name": "Kiki's Pizza",
    "address": "456 Oak St"
  }
}

Error Response (400):
{ "errors": ["Price must be between 1 and 30"] }

Validation Rules

RestaurantPizza:
price: Must be an integer between 1 and 30.
pizza_id: Must reference an existing Pizza.
restaurant_id: Must reference an existing Restaurant.



Postman Usage Instructions

Open Postman.
Click Import → Upload challenge-1-pizzas.postman_collection.json.
Run the requests in the collection to test each endpoint.
Verify responses match the expected formats above.

Project Structure
.
├── server/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── restaurant.py
│   │   ├── pizza.py
│   │   ├── restaurant_pizza.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   ├── restaurant_pizza_controller.py
│   ├── seed.py
├── migrations/
├── challenge-1-pizzas.postman_collection.json
└── README.md

