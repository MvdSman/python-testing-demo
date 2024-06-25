import pytest
import requests


def test_http_logs_are_not_catched(
    capsys,
):
    requests.get("https://www.google.com/")

    out, err = capsys.readouterr()
    print(out)
    assert "HTTP/1.1 200 OK" not in out


def test_http_logs_are_catched(
    debug_http,
    capsys,
):
    requests.get("https://www.google.com/")

    out, err = capsys.readouterr()
    print(out)
    assert "HTTP/1.1 200 OK" in out