import pytest
from starlette.testclient import TestClient

from app.main import create_application


@pytest.fixture(scope="module")
def test_app():
    app = create_application()
    with TestClient(app) as test_client:
        yield test_client
