from app import app
from models import db, Location, Item, LocationItem

with app.app_context():
    db.drop_all()
    db.create_all()

    locations = [
        Location(name="New York"),
        Location(name="San Francisco"),
        Location(name="Los Angeles"),
    ]

    items = [
        Item(name="Laptop"),
        Item(name="Phone"),
        Item(name="Tablet"),
    ]

    db.session.add_all(locations + items)
    db.session.commit()

    location_items = [
        LocationItem(location_id=1, item_id=1, obtained=True),
        LocationItem(location_id=1, item_id=2, obtained=False),
        LocationItem(location_id=2, item_id=3, obtained=True),
        LocationItem(location_id=3, item_id=1, obtained=False),
    ]

    db.session.add_all(location_items)
    db.session.commit()
