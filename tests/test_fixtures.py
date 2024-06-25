import pytest


def test_should_have_access_to_global_variable():
    assert pytest.GLOBAL_TEST_VARIABLE == "test global variable"