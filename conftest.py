import pytest


@pytest.fixture(autouse=True)
def global_setup_fixture():
    print("global setup fixture - executed")
