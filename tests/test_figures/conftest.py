import pytest

from src.figures.circle import Circle
from src.figures.rectangle import Rectangle
from src.figures.square import Square
from src.figures.triangle import Triangle


@pytest.fixture
def create_circle():
    circle = Circle(8)
    yield circle
    del circle


@pytest.fixture
def create_rectangle():
    rectangle = Rectangle(8, 4)
    yield rectangle
    del rectangle


@pytest.fixture
def create_square():
    square = Square(5)
    yield square
    del square


@pytest.fixture
def create_triangle():
    triangle = Triangle(3, 4, 5)
    yield triangle
    del triangle
