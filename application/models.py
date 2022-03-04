#create tables in the database
from application import db

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(40), nullable=False)

    tourist_sites = db.relationship('TouristSites', backref='locations')

class TouristSites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    site_name = db.Column(db.String(50), nullable=False)
    favourite_part = db.Column(db.String(200), nullable=False)