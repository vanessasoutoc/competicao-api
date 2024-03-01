import json
from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)
def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {
        "health": "ok"
    }

def test_success_competicoes_list_all():
    response = client.get("/api/v1/competicoes")
    assert response.status_code == 200
    assert len(json.loads(json.dumps(response.json()))) >= 0

def test_success_competicoes_post():
    data = {"titulo": "Corrida 200 m"}
    response = client.post(
        "/api/v1/competicoes",
        json=data
    )
    assert response.status_code == 201
    assert response.json()["titulo"] == "Corrida 200 m"


def test_success_competicoes_finaliza():
    id = 1
    response = client.patch(
        f'/api/v1/competicoes/{id}/finaliza'
    )
    assert response.status_code == 200

def test_success_pontuacoes_list_all():
    response = client.get("/api/v1/pontuacoes")
    assert response.status_code == 200
    assert len(json.loads(json.dumps(response.json()))) >= 0

def test_error_pontuacoes_post():
    data = {
        "competicao_id": 1,
        "atleta": "Marta Souza",
        "valor": 25.567,
        "unidade": "s"
    }
    response = client.post(
        "/api/v1/pontuacoes",
        json=data
    )
    assert response.status_code == 404

def test_error_pontuacoes_post():
    data = {
        "competicao_id": 1001,
        "atleta": "Marta Souza",
        "valor": 25.567,
        "unidade": "s"
    }
    response = client.post(
        "/api/v1/pontuacoes",
        json=data
    )
    assert response.status_code == 404

def test_success_pontuacoes_post():
    data = {
        "competicao_id": 2,
        "atleta": "Marta Souza",
        "valor": 25.567,
        "unidade": "s"
    }
    response = client.post(
        "/api/v1/pontuacoes",
        json=data
    )
    assert response.status_code == 201
    assert response.json()["atleta"] == "Marta Souza"

def test_success_pontuacoes_update():
    data = {
        "id":2,
        "competicao_id": 2,
        "atleta": "Marta Souza",
        "valor": 20.567,
        "unidade": "s"
    }
    response = client.post(
        "/api/v1/pontuacoes",
        json=data
    )
    assert response.status_code == 201
    assert response.json()["atleta"] == "Marta Souza"
