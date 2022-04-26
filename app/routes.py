from flask import Blueprint, jsonify

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
    return_planet = None
    try:
        planet_id = int(planet_id)
    except ValueError:
        return jsonify({'msg': f"Invalid planet ID: '{planet_id}'. Planet ID must be an integer."}), 400
    for planet in planets:
        if planet.id == planet_id:
            return_planet = {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "moons": planet.moons
            }
    if return_planet is None:
        return jsonify({'msg': f"no planet with id '{planet_id}' found"}), 404
    return jsonify(return_planet)