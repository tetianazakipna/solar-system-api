from flask import Blueprint, jsonify, request, make_response, abort

from app import db
from app.models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        moons=request_body["moons"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet: {new_planet.name} successfully created", 201)

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except: 
        abort(make_response({'msg': f"Invalid planet ID: '{planet_id}'. Planet ID must be an integer."}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({'msg': f"no planet with id '{planet_id}' found"}, 404))
    
    return planet

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    response = []
    planets = Planet.query.all()
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
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "moons": planet.moons
    }