from .figure import Figure


class Square(Figure):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Square side must be a positive values")
        self.side = side

    def get_area(self):
        return self.side**2

    def get_perimeter(self):
        return 4 * self.side
