import json

from flask import request

from . import create_app, database
from .models import Cars

app = create_app()


@app.route('/', methods=['GET'])
def fetch():
    cars = database.get_all(Cars)
    all_cars = []
    for car in cars:
        new_car = {
            "id": car.id,
            "color": car.color,
            "price": car.price,
            "brand": car.brand
        }

        all_cars.append(new_car)

    if (len(all_cars) == 0):
        return json.dumps("No cars found"), 200
    else:
        return json.dumps(all_cars), 200


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    color = data['color']
    price = data['price']
    brand = data['brand']

    database.add_instance(Cars, color=color, price=price, brand=brand)
    return json.dumps("Added"), 200


@app.route('/remove/<car_id>', methods=['DELETE'])
def remove(car_id):
    database.delete_instance(Cars, id=car_id)
    return json.dumps("Deleted"), 200


@app.route('/edit/<car_id>', methods=['PATCH'])
def edit(car_id):
    data = request.get_json()
    new_price = data['price']
    database.edit_instance(Cars, id=car_id, price=new_price)
    return json.dumps("Edited"), 200