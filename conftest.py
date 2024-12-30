import pytest


@pytest.fixture
def global_setup_fixture():
    print("global setup")
