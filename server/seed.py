# seed.py

from app import app
from models import db, Location, Item, LocationItem

# Create the tables
with app.app_context():
    db.create_all()

# Seed data
items_data = [
    {"name": "Pocket Tissues", "cost": 50, "locations": ["Poppo"]},
    {"name": "Paper Plate", "cost": 15, "locations": ["Ebisu Pawn"]},
    {"name": "Iron Plate", "cost": 150, "locations": ["Ebisu Pawn", "Encounters"]},
    {"name": "Bronze Plate", "cost": 1500, "locations": ["Ebisu Pawn", "Encounters"]},
    {"name": "Silver Plate", "cost": 15000, "locations": ["Ebisu Pawn", "Encounters"]},
    {"name": "Gold Plate", "cost": 150000, "locations": ["Ebisu Pawn"]},
    {"name": "Platinum Plate", "cost": 300000, "locations": ["Ebisu Pawn"]},
    {"name": "Homestyle Chicken Cat Food", "cost": 300, "locations": ["Don Quijote", "Poppo (Showa, E. Shichifuku)"]},
    {"name": "Miso Crispy Beef Cat Food", "cost": 300, "locations": ["Don Quijote", "Poppo (Tenkaichi, W. Shichifuku)"]},
    {"name": "Fresh Tuna Cat Food", "cost": 300, "locations": ["Don Quijote", "Poppo (E. Shichifuku)"]},
    {"name": "Cheese Salmon Paté Cat Food", "cost": 300, "locations": ["Don Quijote", "Poppo (Tenkaichi)"]},
    {"name": "White Fish and Sardine Cat Food", "cost": 300, "locations": ["Don Quijote", "Poppo (Showa)"]},
    {"name": "Bonito Flake Cat Food", "cost": 300, "locations": ["Don Quijote", "Poppo (W. Shichifuku)"]},
    {"name": "Gold Tuna Cat Food", "cost": 70, "locations": ["Onodera's Wares"]},
    {"name": "Small Screw", "cost": 200, "locations": ["Poppo", "common pickup"]},
    {"name": "Exquisite Screw", "cost": 600, "locations": ["Ebisu Pawn", "Club SEGA Nakamichi pickup"]}
]

# Clear existing data
with app.app_context():
    db.session.query(LocationItem).delete()
    db.session.query(Item).delete()
    db.session.query(Location).delete()

# Seed locations
location_names = set()
for item in items_data:
    location_names.update(item["locations"])

with app.app_context():
    locations = {name: Location(name=name) for name in location_names}
    db.session.add_all(locations.values())
    db.session.commit()

# Seed items and location items
with app.app_context():
    for item_data in items_data:
        item = Item(name=item_data["name"], cost=item_data["cost"])
        db.session.add(item)
        db.session.commit()

        for location_name in item_data["locations"]:
            location = db.session.query(Location).filter_by(name=location_name).first()
            location_item = LocationItem(location_id=location.id, item_id=item.id)
            db.session.add(location_item)

    db.session.commit()
