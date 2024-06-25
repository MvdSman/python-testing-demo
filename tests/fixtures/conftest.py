import pytest

from python_testing_demo.fixtures import SomeClass

def pytest_configure():
    """
    Set up pytest global variables.
    """
    pytest.GLOBAL_TEST_VARIABLE = "test global variable"
    pytest.GLOBAL_TEST_VARIABLE_APPENDED = f"{pytest.GLOBAL_TEST_VARIABLE}_appended"



@pytest.fixture
def setup_and_teardown_class():
    """
    Sets up a reusable context for the actual tests and tears everything down afterwards.
    """

    # Anything that's set up here will be available during the lower-level test!
    print("Setting up the test context...")
    some_class = SomeClass()
    print(some_class.some_other_var)

    # Run the actual lower-level test
    yield some_class

    # Anything after the yield that was affected during the lower-level test is still in that same context!
    # Note that this can influence other tests if not teared down correctly
    print("Tearing down the test context...")
    print(some_class.some_other_var)



some_global_class = SomeClass()
@pytest.fixture
def incorrectly_setup_and_teardown_class():
    """
    Sets up a reusable context for the actual tests and tears everything down afterwards.
    """

    # Anything that's set up here will be available during the lower-level test!
    print("Setting up the test context...")
    some_class = some_global_class
    print(some_class.some_other_var)

    # Run the actual lower-level test
    yield some_class

    # Anything after the yield that was affected during the lower-level test is still in that same context!
    # Note that this can influence other tests if not teared down correctly
    print("Tearing down the test context...")
    print(some_class.some_other_var)