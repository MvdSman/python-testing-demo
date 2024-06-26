import pytest


def test_should_have_access_to_global_variable():
    assert pytest.GLOBAL_TEST_VARIABLE == "test global variable"
    assert "variable_appended" in pytest.GLOBAL_TEST_VARIABLE_APPENDED


def test_should_use_setup_and_teardown_and_overwrite_higher_level_var(setup_and_teardown_class):
    setup_and_teardown_class.some_other_var = setup_and_teardown_class.some_var
    assert setup_and_teardown_class.some_var == "foo"


def test_should_use_setup_and_teardown_and_overwrite_global_var(incorrectly_setup_and_teardown_class):
    incorrectly_setup_and_teardown_class.some_other_var = incorrectly_setup_and_teardown_class.some_var
    assert incorrectly_setup_and_teardown_class.some_var == "foo"


def test_should_get_overwritten_global_class(incorrectly_setup_and_teardown_class):
    assert incorrectly_setup_and_teardown_class.some_other_var == "foo"