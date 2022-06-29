from starlette.testclient import TestClient

from app import app

client = TestClient(app)


class TestService:
    def test_service_ccaa(self):
        response = client.post("/data/ccaas")
        assert response.status_code == 200
        assert response.json()['length'] == 3
        assert response.json().get('items') is not None

        body = {'query': {
            'column': {
                '==': [1, 2]
            }
        }}
        response = client.post("/data/ccaas", json=body)
        assert response.status_code == 422

        response = client.post("/data/ccaas", json={'query': {'cie': {'2': 2}}})
        assert response.status_code == 422

        response = client.post("/data/ccaas", json={})
        assert response.status_code == 200

    def test_service_cie(self):
        response = client.post("/data/cie")
        assert response.status_code == 200
        assert response.json()['length'] == 4
        assert response.json().get('items') is not None

        response = client.post("/data/cie", json={'query': {'algo': {'(': 2}}})
        assert response.status_code == 422

        response = client.post("/data/cie", json={'query': {'algo': {'(': 2}}})
        assert response.status_code == 422

    def test_service_ages_groups(self):
        response = client.post("/data/ages-groups")
        assert response.status_code == 200
        assert response.json()['length'] == 4

        response = client.post("/data/ages-groups", json={'hola': 2})
        assert response.status_code == 422

        response = client.post("/data/ages-groups&limit=hola")
        assert response.status_code == 404

    def test_service_deceases(self):
        response = client.post("/data/deceases")
        assert response.status_code == 200
        assert response.json()['length'] == 16

    def test_service_diseases(self):
        response = client.post("/data/diseases")
        assert response.status_code == 200
        assert response.json()['length'] == 3

        response = client.post("/data/diseases", json={})
        assert response.status_code == 200

        response = client.post("/data/diseases", json={'query': {'namee': {'==': 2}}})
        assert response.status_code == 422

    def test_service_chart(self):
        response = client.post("/managers/chart4",
                               json={"ccaa": {
                                   "==": 99
                               }})
        assert response.status_code == 404

    def test_service_chart_incorrect_column(self):
        body = {
            "764": {
                "==": 999
            }
        }
        response = client.post("/managers/chart", json=body)
        assert response.status_code == 422

    def test_service_deaths_predictor(self):
        response = client.post("/managers/deaths-predictor")
        assert response.status_code == 400

        response = client.post("/managers/chart&group=22&summ=hola")
        assert response.status_code == 404

    def test_service_deaths_predictor_chart(self):
        response = client.post("/managers/deaths-predictor-chart")
        assert response.status_code == 400

        response = client.post("/managers/deaths-predictor-chart&group=22&summ=hola")
        assert response.status_code == 404
