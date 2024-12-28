import pytest


@pytest.mark.smoke
def test_one():
    print("one")

@pytest.mark.regression
def test_two():
    print("two")

@pytest.mark.login
@pytest.mark.login1
def test_three():
    print("three")
