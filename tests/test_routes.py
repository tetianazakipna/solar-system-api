def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_list_of_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
        "id": 1,
        "name": "Mercury",
        "description": "1 planet from sun",
        "moons": 0
        },
        {
        "id": 2,
        "name": "Venus",
        "description": "2 planet from sun",
        "moons": 0
        }
    ]


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "1 planet from sun",
        "moons": 0
    }

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Earth",
        "description": "The Best!",
        "moons": 1
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet: Earth successfully created"