from math import pi
from lab_python_oop.color import Color
from lab_python_oop.figure import Figure

class Circle(Figure):
    def __init__(self, radius_: float, color_: Color):
        self.radius = radius_
        self.color = color_
        self.name = "Круг"

    def get_area(self) -> float:
        return pi * self.radius ** 2
    
    def __repr__(self):
        return "{}: радиус: {}, цвет: {}".format(self.name, self.radius, self.color)