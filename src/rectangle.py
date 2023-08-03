from src.figure import Figure, ImpossibleFigureError


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.validate_args(side_a=side_a, side_b=side_b)
        self.__side_a = side_a
        self.__side_b = side_b

    def validate_args(self, side_a, side_b):
        if any([side_a <= 0, side_b <= 0]):
            raise ImpossibleFigureError(f'Can not create {self.__class__.__name__} with sides: {side_a, side_b}')

    @property
    def area(self) -> float:
        return self.__side_a * self.__side_b

    @property
    def perimeter(self) -> float:
        return 2 * (self.__side_a + self.__side_b)


r = Rectangle(8, 4)
print(r.area)
