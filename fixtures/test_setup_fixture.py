import pytest


@pytest.fixture
def setup_and_teardown():
    print("setup fixture executed")
    yield
    print("tear down executed")


def test_setup_fixture(setup_and_teardown):
    print("test executed")