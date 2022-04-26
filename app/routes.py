from re import A
from flask import Blueprint, jsonify, abort, make_response

class Planets:
    
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons
    
planets = [
    Planets(1, "Mercury", "first planet from the sun", 0),
    Planets(2, "Venus", "second planet from the sun", 0),
    Planets(3, "Earth", "third planet from the sun", 1),
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except: 
        abort(make_response({'msg': f"Invalid planet ID: '{planet_id}'. Planet ID must be an integer."}, 400))
    for planet in planets:
        if planet.id == planet_id:
            return planet
    abort(make_response({'msg': f"no planet with id '{planet_id}' found"}, 404))

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    response = []
    for planet in planets:
        response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "moons": planet.moons
            }
        ) 
    return jsonify(response), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify({
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "moons": planet.moons
    })