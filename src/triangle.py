import math
from .figure import Figure


class Triangle(Figure):
    def __init__(self, side_1, side_2, side_3):
        if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
            raise ValueError("Side must be a positive value")
        if (
            side_1 + side_2 <= side_3
            or side_1 + side_3 <= side_2
            or side_2 + side_3 <= side_1
        ):
            raise ValueError("It is impossible to create a triangle with such sides")
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def get_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def get_area(self):
        perimeter = self.get_perimeter() / 2
        return math.sqrt(
            perimeter
            * (perimeter - self.side_1)
            * (perimeter - self.side_2)
            * (perimeter - self.side_3)
        )
