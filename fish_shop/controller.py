from main import app, db
from models import Fish, FishSchema
from flask import request, jsonify
from marshmallow.exceptions import ValidationError

fish_schema = FishSchema()
fishes_schema = FishSchema(many = True)

@app.route('/')
def index():
    return "Whaaat uuuuuuuup?"

@app.route('/fish/<id>')
def get_fish(id):
    fish = Fish.query.get(id)
    if fish is None:
        return{"errors": "No fish with id: {0} present".format(id)}, 404
    response = fish_schema.dump(fish)
    return jsonify(response)

@app.route('/fish', methods=['GET'])
def get_all_fishes():
    response = fishes_schema.dump(Fish.query.all())
    return jsonify(response)

@app.route('/fish', methods=['POST'])
def create_fish():
    try:
        fish = Fish(**fish_schema.load(request.get_json()))
    except ValidationError as err:
        return {"errors": err.messages}, 422
    db.session.add(fish)
    db.session.commit()
    response = fish_schema.dump(fish)
    return jsonify(response)
