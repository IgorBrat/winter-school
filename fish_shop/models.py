from typing import List
from main import db, ma

class Fish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    origin = db.Column(db.String(20))
    age_in_months = db.Column(db.Integer)
    weight_in_grams = db.Column(db.Integer)

class FishSchema(ma.Schema):
    class Meta:
        fields = ('name', 'origin')
        
