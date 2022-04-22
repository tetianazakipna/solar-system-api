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