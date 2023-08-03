class ImpossibleFigureError(ValueError):
    pass


class Figure:
    def __init__(self):
        self.name = self.__class__.__name__

    def validate_args(self, *args):
        raise NotImplementedError

    @staticmethod
    def validate_figure(figure):
        if not isinstance(figure, Figure):
            raise ValueError(f'Incorrect class passed. {figure.__class__.__name__} is not {Figure.__name__}')

    @property
    def area(self):
        raise NotImplementedError

    @property
    def perimeter(self):
        raise NotImplementedError

    def add_area(self, figure):
        self.validate_figure(figure=figure)
        return self.area + figure.area
