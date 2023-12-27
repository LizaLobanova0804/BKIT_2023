from lab_python_oop.color import Color
from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, length_: float, color_: Color):
        self.length = length_
        self.color = color_
        self.name = "Квадрат"

    def get_area(self) -> float:
        return self.length ** 2

    def __repr__(self):
        return "{}: сторона: {}, цвет: {}".format(self.name, self.length, self.color)
