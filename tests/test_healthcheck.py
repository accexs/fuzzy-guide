def test_is_alive(test_app):
    response = test_app.get("/healthcheck")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
