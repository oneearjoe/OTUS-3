import pytest

from src.square import Square


@pytest.mark.parametrize("side, expected", [(1, 4), (1.5, 6)])
def test_square_perimeter_positive(side, expected):
    square = Square(side)

    assert square.get_perimeter() == expected, "Incorrect perimeter"


@pytest.mark.parametrize("side, expected", [(1, 1), (1.5, 2.25)])
def test_square_area_positive(side, expected):
    square = Square(side)

    assert round(square.get_area(), 3) == expected, "Incorrect perimeter"


@pytest.mark.parametrize(
    "side, expected_exception", [(-1, ValueError), (0, ValueError), ("a", TypeError)]
)
def test_square_validation(side, expected_exception):
    with pytest.raises(expected_exception):
        Square(side)
