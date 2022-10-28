"""Test worker."""

from dispatcher.worker import execute


def test_execute():
    result = execute("echo Test")
    for key in ["stderr", "stdout"]:
        result[key] = result.get(key, "").strip()
    assert result == {
        "cmnd": "echo Test",
        "code": 0,
        "stderr": "",
        "stdout": "Test",
    }
