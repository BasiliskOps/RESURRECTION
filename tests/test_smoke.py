from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_index():
    assert client.get("/").status_code == 200


def test_run_requires_payment():
    r = client.post("/api/v1/runs", json={"question": "why do naked mole rats barely age"})
    assert r.status_code == 402


def test_findings_are_free():
    assert client.get("/api/v1/findings").status_code == 501
