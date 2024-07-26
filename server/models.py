from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    items = db.relationship('LocationItem', back_populates='location')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            # Only include basic info to avoid recursion
            'items': [{'id': item.item.id, 'name': item.item.name} for item in self.items]
        }

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    locations = db.relationship('LocationItem', back_populates='item')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            # Only include basic info to avoid recursion
            'locations': [{'id': location.location.id, 'name': location.location.name} for location in self.locations]
        }

class LocationItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    obtained = db.Column(db.Boolean, default=False)
    location = db.relationship('Location', back_populates='items')
    item = db.relationship('Item', back_populates='locations')

    def to_dict(self):
        return {
            'id': self.id,
            'location_id': self.location_id,
            'item_id': self.item_id,
            'obtained': self.obtained
        }
