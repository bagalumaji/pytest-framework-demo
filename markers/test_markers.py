import pytest


@pytest.mark.login
def test_marker_login():
    print("test markers login")


@pytest.mark.xfail
def test_fail():
    print("fail")
    assert False


@pytest.mark.xfail
def test_expected_pass():
    print("expected pass")


@pytest.mark.skip
def test_skip():
    print("skip test")
