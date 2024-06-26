from python_testing_demo.coverage import untested_function


def test_untested_function_true():
    assert untested_function(runme=True) is None