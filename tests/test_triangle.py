import pytest

from src.triangle import Triangle


@pytest.mark.parametrize(
    "side_1, side_2, side_3, expected",
    [
        (3, 4, 5, 12),
        (5, 5, 5, 15),
        (5, 5, 6, 16),
    ],
    ids=["right", "equilateral", "isosceles"],
)
def test_triangle_perimeter_positive(side_1, side_2, side_3, expected):
    triangle = Triangle(side_1, side_2, side_3)

    assert triangle.get_perimeter() == expected, "Incorrect perimeter"


@pytest.mark.parametrize(
    "side_1, side_2, side_3, expected",
    [
        (3, 4, 5, 6.0),
        (5, 5, 5, 10.825),
        (5, 5, 6, 12.0),
    ],
    ids=["right", "equilateral", "isosceles"],
)
def test_triangle_area_positive(side_1, side_2, side_3, expected):
    triangle = Triangle(side_1, side_2, side_3)
    assert round(triangle.get_area(), 3) == expected, "Incorrect area"


@pytest.mark.parametrize(
    "side_1, side_2, side_3, expected_exception",
    [
        (-1, 2, 3, ValueError),
        (2, 3, 5, ValueError),
        (2, 0, 5, ValueError),
        ("a", 2, 3, TypeError),
    ],
)
def test_triangle_validation(side_1, side_2, side_3, expected_exception):
    with pytest.raises(expected_exception):
        Triangle(side_1, side_2, side_3)
