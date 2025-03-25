import pytest
from src.circle import Circle
from src.rectangle import Rectangle
from src.triangle import Triangle
from src.square import Square


@pytest.mark.parametrize(
    "figure1, figure2, expected_sum",
    [
        (Circle(1), Circle(2), 15.708),
        (Rectangle(2, 4), Rectangle(1, 3), 11),
        (Triangle(3, 4, 5), Circle(1), 9.142),
        (Square(2), Square(3), 13),
        (Square(2.5), Circle(1), 9.392),
        (Square(3), Triangle(3, 4, 5), 15.0),
    ],
)
def test_add_area_positive(figure1, figure2, expected_sum):
    assert round(figure1.add_area(figure2), 3) == expected_sum


@pytest.mark.parametrize(
    "invalid_figure",
    [
        "not_a_figure",
        123,
        None,
        {"shape": "circle"},
    ],
    ids=["string", "number", "none", "dict"],
)
def test_add_area_negative(invalid_figure):
    circle = Circle(1)
    with pytest.raises(ValueError, match="Invalid figure"):
        circle.add_area(invalid_figure)
