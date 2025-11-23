MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
"""


def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)
