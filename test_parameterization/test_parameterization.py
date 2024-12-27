import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (3, 2, 5)
])
def test_add_with_parameter(a, b, expected):
    assert add(a, b) == expected
