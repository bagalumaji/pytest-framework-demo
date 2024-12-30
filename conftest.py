import pytest


@pytest.fixture(autouse=True,scope="function")
def global_setup_fixture():
    print("global setup fixture - executed")
