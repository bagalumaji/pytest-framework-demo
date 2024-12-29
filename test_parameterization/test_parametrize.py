import pytest


@pytest.mark.parametrize("value", [1, 2, 3])
def test_parametrize(value):
    print(f"value : {value}")
