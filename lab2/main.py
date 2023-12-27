from lab_python_oop.circle import Circle
from lab_python_oop.color import Color
from lab_python_oop.square import Square
from lab_python_oop.rectangle import Rectangle

if __name__ == "__main__":
    print(Rectangle(9, 4, Color("Желтый")))
    print(Circle(9, Color("Белый")))
    print(Square(9, Color("красный")))