import pytest


@pytest.mark.smoke
def test_sample_demo_1():
    print("demo test")


@pytest.mark.skip
def test_skip():
    print("skip test")