# x-api-key: pub_eeeaade4c21da85cda07bef9b688725ae5796d2be74b5e4fee5e7f9e477e1899

import requests

def test_obtener_usuario():
    url = "https://reqres.in/api/users/2"

    header = {
        "x-api-key": "pub_eeeaade4c21da85cda07bef9b688725ae5796d2be74b5e4fee5e7f9e477e1899"
    }

    response = requests.get(url, headers=header)
    
    codigo = response.status_code
    assert codigo == 200

    assert "application/json" in response.headers["Content-Type"]

    data = response.json()

    assert isinstance(data,dict)
    assert "data" in data
    assert isinstance(data["data"],dict)


    assert "id" in data["data"]
    assert "email" in data["data"]
    assert "first_name" in data["data"]
    assert "last_name" in data["data"]

    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"

    assert response.elapsed.total_seconds() < 2

def test_crear_usuario():
    url = "https://reqres.in/api/users/"

    header = {
            "x-api-key": "pub_eeeaade4c21da85cda07bef9b688725ae5796d2be74b5e4fee5e7f9e477e1899"
        }

    usuario = {
        "email": "mail@gmail.com",
        "first_name": "Pepe",
        "last_name": "Pepito"
    }

    response = requests.post(url,headers=header,json=usuario)

    assert response.status_code == 201

    assert "application/json" in response.headers["Content-Type"]

    data = response.json()
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data
    

    assert data["email"] == usuario["email"]
    assert data["first_name"] == usuario["first_name"]
    assert data["last_name"] == usuario["last_name"]
 
