import pytest
from pf54 import check_anagram

values = [('eat', 'tea', True), ('backward', 'drawback', False),
          ('Reductions', 'discounter', True), ('About', 'table', False)]


@pytest.mark.parametrize("data1,data2,expected_value", values)
def test_case(data1, data2, expected_value):
    result = check_anagram(data1, data2)
    assert result == expected_value
