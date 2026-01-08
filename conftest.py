import pytest

MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
"""


def pytest_configure(config) -> None:
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)


@pytest.fixture(autouse=True)
def go_to_tmpdir(request) -> any:
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield


@pytest.fixture
def csv_file(tmp_path, request) -> str:
    content = request.param
    file = tmp_path / "input.csv"
    file.write_text(content)
    return file
