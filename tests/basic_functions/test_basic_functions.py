import pytest
from python_testing_demo.basic_functions import function_that_returns_text


def test_str():
    assert function_that_returns_text("You should see this text!") == "You should see this text!"


def test_int_as_str():
    assert function_that_returns_text("15") == "15"


@pytest.mark.issue
def test_int():
    assert function_that_returns_text(15) == "15"


@pytest.mark.fix
def test_int_should_fail():
    with pytest.raises(ValueError, match="Input did not have a"):
        assert function_that_returns_text(15) == "15"


@pytest.mark.fix
@pytest.mark.parametrize(
    "input, output, raises_error",
    [
        (
            "some text",
            "some text",
            False,
        ),
        (
            15,
            None,
            True,
        )
    ],
    ids=["will_return_text","will_fail_on_non-str_type"],
)
def test_function_that_returns_text(input, output, raises_error):
    if raises_error:
        with pytest.raises(ValueError, match="Input did not have a"):
            function_that_returns_text(input)
    else:
        assert function_that_returns_text(input) == output