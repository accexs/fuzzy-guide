def test_avg_coalesce(test_app):
    response = test_app.get("/coalesce/1?action=avg")

    assert response.status_code == 200
    assert response.json() == {"deductible": 1066, "stop_loss": 11000, "oop_max": 5666}


def test_sum_coalesce(test_app):
    response = test_app.get("/coalesce/1?action=sum")

    assert response.status_code == 200
    assert response.json() == {"deductible": 3200, "stop_loss": 33000, "oop_max": 17000}


def test_avg_coalesce_bad_member_id(test_app):
    response = test_app.get("/coalesce/s")

    assert response.status_code == 422


def test_max_by_key_coalesce(test_app):
    response = test_app.get("/coalesce/1?key=deductible&action=max_by")
    assert response.status_code == 200
    assert response.json()["deductible"] == 1200


def test_min_by_key_coalesce(test_app):
    response = test_app.get("/coalesce/1?key=stop_loss&action=min_by")
    assert response.status_code == 200
    assert response.json()["stop_loss"] == 10000


def test_avg_coalesce_bad_key(test_app):
    response = test_app.get("/coalesce/1?bad=key")
    assert response.status_code == 422
    pass
