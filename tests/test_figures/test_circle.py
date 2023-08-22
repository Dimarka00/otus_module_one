import pytest

from src.figures.circle import Circle
from src.figures.figure import Figure, ImpossibleFigureError


def test_circle_init(create_circle):
    assert isinstance(create_circle, Figure) is True


def test_circle_name(create_circle):
    assert create_circle.name == 'Circle'


def test_circle_area(create_circle):
    assert create_circle.area == 201


def test_circle_perimeter(create_circle):
    assert create_circle.perimeter == 50


def test_circle_add_circle_area(create_circle):
    assert create_circle.add_area(create_circle) == 402


def test_circle_add_rectangle_area(create_circle, create_rectangle):
    assert create_circle.add_area(create_rectangle) == 233


def test_circle_add_square_area(create_circle, create_square):
    assert create_circle.add_area(create_square) == 226


def test_circle_add_triangle_area(create_circle, create_triangle):
    assert create_circle.add_area(create_triangle) == 207


def test_create_circle_bad_radius():
    with pytest.raises(ImpossibleFigureError):
        Circle(radius=-13)


def test_circle_zero_radius(create_circle):
    with pytest.raises(ImpossibleFigureError):
        Circle(radius=0)


