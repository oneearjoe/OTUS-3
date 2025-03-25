import pytest

from src.circle import Circle


@pytest.mark.parametrize("radius, expected", [(1, 6.28), (10.5, 65.97)])
def test_circle_perimeter_positive(radius, expected):
    circle = Circle(radius)

    assert round(circle.get_perimeter(), 2) == expected, "Incorrect perimeter"


@pytest.mark.parametrize("radius, expected", [(1, 3.14), (10.5, 346.36)])
def test_circle_area_positive(radius, expected):
    circle = Circle(radius)

    assert round(circle.get_area(), 2) == expected, "Incorrect area"


@pytest.mark.parametrize(
    "radius, expected_exception",
    [
        (-1, ValueError),
        (0, ValueError),
        ("a", TypeError),
    ],
)
def test_circle_validation(radius, expected_exception):
    with pytest.raises(expected_exception):
        Circle(radius)
