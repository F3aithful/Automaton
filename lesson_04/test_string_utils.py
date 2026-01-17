import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# --------------------------Тест №1 "Capitalize"--------------------------


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("123", "123"),
    ("vlad thinking", "Vlad thinking"),])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ('[]', '[]'),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# --------------------------Тест №2 "Trim"--------------------------


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   Moscow", "Moscow"),
    ("   123", "123"),
    ("   Vlad Buchko", "Vlad Buchko"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
    ("   $%$GFT123", "$%$GFT123"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# --------------------------Тест №3 "Contains"--------------------------


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Vlad", "V", True),
    ("Maria", "i", True),
    ('1234', '3', True)
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("Vl@d", "a", False),
    ("", " ", False),
    ('ffffff', 'F', False)
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# --------------------------Тест №4 "Delete_symbol"--------------------------


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Simferopol", "p", "Simferool"),
    ("Hellow", "H", "ellow"),
    ('ffddff', 'f', "dd")
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("Simferopol", "H", "Simferopol"),
    ("Hellow", "HHelloww", "Hellow"),
    ('ffddff', '@', "ffddff")
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
