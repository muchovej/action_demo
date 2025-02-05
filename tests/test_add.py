from src.add import add
import pytest

@pytest.mark.parametrize(
    "input1, input2, expected_value",
    [(3, 2, 5), (-3, -2, -5), (-3, 2, -1), (4,5,9)],
)
def test_add(input1, input2, expected_value):
    assert add(input1, input2) == expected_value
