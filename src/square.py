from src.figure import Figure


class Square(Figure):
    def __init__(self, side, name):
        super().__init__(name)
        self.validate_args(side=side)
        self.__side = side

    def validate_args(self, side):
        if side <= 0:
            raise ValueError(f'Can not create {self.name} with side {side}')

    @property
    def area(self) -> float:
        return self.__side ** 2

    @property
    def perimeter(self) -> float:
        return self.__side * 4


# s = Square(10, 'Square')
# print(s.area)
# t = Triangle(13, 14, 15, 'Triangle')
# print(t.area)
# print(t.add_area(s))

