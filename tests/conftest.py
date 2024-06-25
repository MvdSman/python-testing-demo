import pytest


def pytest_configure():
    """
    Set up pytest global variables.
    """
    pytest.GLOBAL_TEST_VARIABLE = "test global variable"