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

@app.route('/locations', methods=['GET'])
def get_locations():
    locations = Location.query.all()
    return jsonify([location.to_dict() for location in locations])

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

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

if __name__ == '__main__':
    app.run(debug=True)
