import pytest


@pytest.fixture(params=[1, 2, 3])
def one_value(request):
    return request.param


def test_one_value(one_value):
    print(f"this is the current value : {one_value}")
    assert one_value in [1, 2, 3]


@pytest.fixture(params=["one", "two", "three"])
def value(request):
    return request.param


def test_one_string_value(value):
    print(f"current string : {value}")
    assert value in ["one", "two", "three"]