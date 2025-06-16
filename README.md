# Pizza API Challenge

This is a Flask-based RESTful API for managing restaurants, pizzas, and their associations, built using the MVC (Model-View-Controller) pattern.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/pizza-api-challenge.git
   cd pizza-api-challenge

2. **Set Up Virtual Environment: Install dependencies using pipenv:
#pipenv install flask flask_sqlalchemy flask_migrate
#pipenv shell

3. Set Flask Environment Variable:
#export FLASK_APP=server/app.py

4. DB Migration & Seeding Instructions
#flask db init
#flask db migrate -m "Initial migration"
#flask db upgrade

5. Seed the Database: Populate the database with initial data:
#python server/seed.py

6. Run the Application: Start the Flask server:
#python server/app.py

Route Summary

-GET /restaurants: Retrieve a list of all restaurants.
-GET /restaurants/<id></id>: Retrieve details of a specific restaurant, including its associated pizzas.
-DELETE /restaurants/<id></id>: Delete a restaurant and its associated RestaurantPizza entries.
-GET /pizzas: Retrieve a list of all pizzas.
-POST /restaurant_pizzas: Create a new RestaurantPizza association between a restaurant and a pizza.

Example Requests & Responses
-GET /restaurants
1. Request:
GET http://localhost:5000/restaurants
Response (200 OK):
json
[
    {
        "id": 1,
        "name": "Kiki's Pizza",
        "address": "123 Main St",
        "pizzas": [
            {
                "id": 1,
                "name": "Margherita",
                "ingredients": "Dough, Tomato Sauce, Cheese, Basil"
            },
            {
                "id": 2,
                "name": "Pepperoni",
                "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
            }
        ]
    },
    {
        "id": 2,
        "name": "Pizza Palace",
        "address": "456 Oak Ave",
        "pizzas": [
            {
                "id": 1,
                "name": "Margherita",
                "ingredients": "Dough, Tomato Sauce, Cheese, Basil"
            }
        ]
    }
]

2. GET /pizzas
Request:
GET http://localhost:5000/pizzas
json

[
    {
        "id": 1,
        "name": "Margherita",
        "ingredients": "Dough, Tomato Sauce, Cheese, Basil"
    },
    {
        "id": 2,
        "name": "Pepperoni",
        "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
]

#Validation Rules

-RestaurantPizza.price: Must be an integer between 1 and 30 (inclusive).
-RestaurantPizza creation: Both restaurant_id and pizza_id must correspond to existing Restaurant and Pizza records.
-Cascading Deletes: Deleting a Restaurant automatically deletes its associated RestaurantPizza entries.

#Postman Usage Instructions

-Open Postman.
-Click Import in the top-left corner.
-Upload the challenge-1-pizzas.postman_collection.json file located in the project root.
-Use the imported collection to test all API endpoints:
-GET /restaurants
-GET /restaurants/<id></id>
-DELETE /restaurants/<id></id>
-GET /pizzas
-POST /restaurant_pizzas
-Ensure the Flask server is running (python server/app.py) before sending requests.
-Verify responses match the expected formats and status codes as described above.