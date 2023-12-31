from src.figures.figure import Figure, ImpossibleFigureError


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        self.validate_args(side_a=side_a, side_b=side_b, side_c=side_c)
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def validate_args(self, side_a: float, side_b: float, side_c: float):
        if not all([side_a + side_b > side_c, side_b + side_c > side_a, side_c + side_a > side_b]):
            raise ImpossibleFigureError(f'Cannot create {self.__class__.__name__} with sides: {side_a, side_b, side_c}')

    @property
    def area(self) -> float:
        half_perimeter = (self.__side_a + self.__side_b + self.__side_c) / 2
        return (half_perimeter * (half_perimeter - self.__side_a)
                               * (half_perimeter - self.__side_b)
                               * (half_perimeter - self.__side_c)) ** 0.5

    @property
    def perimeter(self) -> float:
        return sum([self.__side_a, self.__side_b, self.__side_c])


t = Triangle(3, 4, 5)
print(t.area)
