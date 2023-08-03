import math

from src.figure import Figure, ImpossibleFigureError


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.validate_args(radius=radius)
        self.__radius = radius

    def validate_args(self, radius):
        if radius <= 0:
            raise ImpossibleFigureError(f'Can not create {self.__class__.__name__} with radius {radius}')

    @property
    def area(self) -> float:
        return round(math.pi * (self.__radius ** 2))

    @property
    def perimeter(self) -> float:
        return round(2 * math.pi * self.__radius)


c = Circle(8)
print(c.area)
print(c.perimeter)

