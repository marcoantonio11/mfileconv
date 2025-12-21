import os

import pytest

from mfileconv.core import csv_to_dict


@pytest.mark.unit
@pytest.mark.parametrize(
    "csv_file", ["name,age\nJoao,20\nMaria,25\n"], indirect=True
)
def test_basic_csv(csv_file) -> None:
    """Tests a basic CSV file with two registers"""
    result = csv_to_dict(str(csv_file))

    assert result == [
        {"name": "Joao", "age": "20"},
        {"name": "Maria", "age": "25"},
    ]


@pytest.mark.unit
@pytest.mark.parametrize(
    "csv_file",
    ["name,address.street,address.number\nJoao,Rua A,45\n"],
    indirect=True,
)
def test_nested_headers(csv_file) -> None:
    """Tests if 'key.subkey' is transformed into a nested dict"""
    result = csv_to_dict(str(csv_file))

    assert result == [
        {"name": "Joao", "address": {"street": "Rua A", "number": "45"}}
    ]


@pytest.mark.unit
@pytest.mark.parametrize(
    "csv_file", ["name,age\nJoao,30\n\nMaria,25\n"], indirect=True
)
def test_ignores_empty_lines(csv_file) -> None:
    """Tests if the function skips empty lines"""
    result = csv_to_dict(str(csv_file))

    assert result == [
        {"name": "Joao", "age": "30"},
        {"name": "Maria", "age": "25"},
    ]


@pytest.mark.unit
@pytest.mark.parametrize(
    "csv_file", ["name,age\nJoao,\nMaria,40\n"], indirect=True
)
def test_missing_values(csv_file) -> None:
    """Tests if missing values are filled with an empty string"""
    result = csv_to_dict(str(csv_file))

    assert result == [
        {"name": "Joao", "age": ""},
        {"name": "Maria", "age": "40"},
    ]


@pytest.mark.unit
@pytest.mark.parametrize(
    "csv_file", ["name,age\nJoao,30,Rua A\n"], indirect=True
)
def test_extra_values_ignored(csv_file) -> None:
    """Tests if extra values are ignored"""
    result = csv_to_dict(str(csv_file))

    assert result == [{"name": "Joao", "age": "30"}]


@pytest.mark.unit
@pytest.mark.parametrize("csv_file", [""], indirect=True)
def test_empty_file_returns_empty_list(csv_file) -> None:
    """Tests if a empty file returns a empty list"""
    result = csv_to_dict(str(csv_file))

    assert result == []


@pytest.mark.unit
@pytest.mark.parametrize("csv_file", ["name,age\n"], indirect=True)
def test_only_header(csv_file) -> None:
    """Tests if the file contains only headers"""
    result = csv_to_dict(str(csv_file))

    assert result == []


@pytest.mark.unit
@pytest.mark.parametrize(
    "csv_file", ["name   , age\nJoao,30\n"], indirect=True
)
def test_headers_with_spaces(csv_file) -> None:
    """Tests headers with spaces"""
    result = csv_to_dict(str(csv_file))

    assert result == [{"name": "Joao", "age": "30"}]


@pytest.mark.unit
def test_file_not_found() -> None:
    """Tests if the file was not found"""
    with pytest.raises(SystemExit) as e:
        csv_to_dict("non_existent_file.csv")

    assert e.value.code == 1


@pytest.mark.unit
@pytest.mark.parametrize("csv_file", ["name,age\nJoao,30\n"], indirect=True)
def test_permission_error(csv_file) -> None:
    "Tests if the file does not have read permission"
    os.chmod(csv_file, 0)

    with pytest.raises(SystemExit) as e:
        csv_to_dict(str(csv_file))

    assert e.value.code == 2


@pytest.mark.unit
@pytest.mark.parametrize(
    "csv_file", ["name,age\nJoao,Pedro,30\n"], indirect=True
)
def test_values_with_comma(csv_file) -> None:
    """Test values with comma"""
    result = csv_to_dict(str(csv_file))

    assert result == [{"name": "Joao", "age": "Pedro"}]


@pytest.mark.unit
@pytest.mark.parametrize("csv_file", ["a.b.c,d.e\nx,y\n"], indirect=True)
def test_multi_level_keys(csv_file):
    """Tests multi level keys"""
    result = csv_to_dict(str(csv_file))

    assert result == [{"a": {"b": {"c": "x"}}, "d": {"e": "y"}}]
