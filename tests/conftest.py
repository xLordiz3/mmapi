from fastapi.testclient import TestClient
import pytest
from mm.app import createApp

@pytest.fixture()
def appClient():
    app = createApp()
    yield TestClient(app)
