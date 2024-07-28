# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    location_items = db.relationship('LocationItem', backref='location', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    location_items = db.relationship('LocationItem', backref='item', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'cost': self.cost
        }

class LocationItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    obtained = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'location_id': self.location_id,
            'item_id': self.item_id,
            'obtained': self.obtained
        }
