import pytest

from src.rectangle import Rectangle


@pytest.mark.parametrize("width, height, expected", [(2, 4, 12), (2.2, 4.4, 13.2)])
def test_rectangle_perimeter_positive(width, height, expected):
    rectangle = Rectangle(width, height)

    assert round(rectangle.get_perimeter(), 3) == expected, "Incorrect perimeter"


@pytest.mark.parametrize("width, height, expected", [(2, 4, 8), (2.2, 4.4, 9.68)])
def test_rectangle_area_positive(width, height, expected):
    rectangle = Rectangle(width, height)

    assert round(rectangle.get_area(), 3) == expected, "Incorrect perimeter"


@pytest.mark.parametrize(
    "width, height, expected_exception",
    [(-1, 2, ValueError), (3, 0, ValueError), ("a", 2, TypeError)],
)
def test_rectangle_validation(width, height, expected_exception):
    with pytest.raises(expected_exception):
        Rectangle(width, height)
