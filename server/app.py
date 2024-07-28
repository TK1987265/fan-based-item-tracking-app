

from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Location, Item, LocationItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)  

@app.route('/')
def index():
    return "Welcome to the API"

@app.route('/locations', methods=['GET'])
def get_locations():
    locations = Location.query.all()
    return jsonify([location.to_dict() for location in locations])

@app.route('/locations', methods=['POST'])
def create_location():
    data = request.get_json()
    new_location = Location(name=data['name'])
    db.session.add(new_location)
    db.session.commit()
    return jsonify(new_location.to_dict()), 201

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'], cost=data['cost'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.get_json()
    item = Item.query.get(id)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    item.name = data.get('name', item.name)
    item.cost = data.get('cost', item.cost)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get(id)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    db.session.delete(item)
    db.session.commit()
    return '', 204

@app.route('/locationitems', methods=['GET'])
def get_location_items():
    location_items = LocationItem.query.all()
    return jsonify([location_item.to_dict() for location_item in location_items])

@app.route('/locationitems', methods=['POST'])
def create_location_item():
    data = request.get_json()
    new_location_item = LocationItem(
        location_id=data['location_id'],
        item_id=data['item_id'],
        obtained=data.get('obtained', False)
    )
    db.session.add(new_location_item)
    db.session.commit()
    return jsonify(new_location_item.to_dict()), 201

@app.route('/locationitems/<int:id>', methods=['PUT'])
def update_location_item(id):
    data = request.get_json()
    location_item = LocationItem.query.get(id)
    if location_item is None:
        return jsonify({'error': 'LocationItem not found'}), 404
    location_item.location_id = data.get('location_id', location_item.location_id)
    location_item.item_id = data.get('item_id', location_item.item_id)
    location_item.obtained = data.get('obtained', location_item.obtained)
    db.session.commit()
    return jsonify(location_item.to_dict())

@app.route('/locationitems/<int:id>', methods=['DELETE'])
def delete_location_item(id):
    location_item = LocationItem.query.get(id)
    if location_item is None:
        return jsonify({'error': 'LocationItem not found'}), 404
    db.session.delete(location_item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

