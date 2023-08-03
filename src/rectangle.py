from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b, name):
        super().__init__(name)
        self.validate_args(side_a=side_a, side_b=side_b)
        self.__side_a = side_a
        self.__side_b = side_b

    def validate_args(self, side_a, side_b):
        if any([side_a <= 0, side_b <= 0]):
            raise ValueError(f'Can not create {self.name} with sides: {side_a, side_b}')

    @property
    def area(self) -> float:
        return self.__side_a * self.__side_b

    @property
    def perimeter(self) -> float:
        return 2 * (self.__side_a + self.__side_b)


r = Rectangle(8, 4, "Rectangle")
print(r.area)
