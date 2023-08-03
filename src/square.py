from src.figure import Figure, ImpossibleFigureError


class Square(Figure):
    def __init__(self, side):
        super().__init__()
        self.validate_args(side=side)
        self.__side = side

    def validate_args(self, side):
        if side <= 0:
            raise ImpossibleFigureError(f'Can not create {self.__class__.__name__} with side {side}')

    @property
    def area(self) -> float:
        return self.__side ** 2

    @property
    def perimeter(self) -> float:
        return self.__side * 4


# s = Square(10)
# print(s.area)
# t = Triangle(13, 14, 15)
# print(t.area)
# print(t.add_area(s))

