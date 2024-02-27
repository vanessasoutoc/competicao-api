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

def test_competicoes_list_all():
    response = client.get("/api/v1/competicoes")
    print(response.json())
    assert response.status_code == 200
    assert len(json.loads(json.dumps(response.json()))) >= 0

def test_competicoes_post():
    data = {"titulo": "Corrida 200 m"}
    response = client.post(
        "/api/v1/competicoes",
        json=data
    )
    assert response.status_code == 201
    assert response.json()["titulo"] == "Corrida 200 m"

def test_pontuacoes_list_all():
    response = client.get("/api/v1/pontuacoes")
    assert response.status_code == 200
    assert len(json.loads(json.dumps(response.json()))) >= 0

def test_pontuacoes_post():
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
    assert response.status_code == 201
    assert response.json()["atleta"] == "Marta Souza"
