import logging
import pytest


@pytest.fixture
def debug_http(scope="module", autouse=False):
    """
    Catches all out-going HTTP calls and prints them in the console.
    Use `autouse=True` to automatically use it in every test which imports this conftest.py file.
    """
    import http.client as http_client

    http_client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger("debug_http").setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True