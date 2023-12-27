from lab_python_oop.color import Color
from lab_python_oop.figure import Figure

class Rectangle(Figure):
    def __init__(self, width_: float, height_: float, color_: Color):
        self.width = width_
        self.height = height_
        self.color = color_
        self.name = "Прямоугольник"

    def get_area(self) -> float:
        return self.width * self.height
    
    def __repr__(self):
        return "{}: ширина: {}, высота: {}, цвет: {}".format(self.name, self.width, self.height, self.color)