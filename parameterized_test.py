import pytest
from boarding1 import boarding

values = [(0, -1), (1, 1), (2, 1), (24, 1), (25, 1), (26, 2), (27, 2),
          (99, 2), (100, 2), (101, 3), (102, 3), (199, 3), (200, 3), (201, -1)]


@pytest.mark.parametrize("seat_number,expected_value", values)
def test_case(seat_number, expected_value):
    result = boarding(seat_number)
    assert result == expected_value
