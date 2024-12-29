import pytest


@pytest.fixture
def setup():
    print("setup fixture executed")


def test_setup_fixture(setup):
    print("test executed")