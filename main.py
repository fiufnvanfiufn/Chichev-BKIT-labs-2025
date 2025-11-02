from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square
from colorama import Fore, Style, init

def create_shapes(size):
    return [
        Rectangle(size, size, "синий"),
        Circle(size, "зеленый"),
        Square(size, "красный")
    ]

def format_shapes(shapes):
    init(autoreset=True)
    colors = [Fore.BLUE, Fore.GREEN, Fore.RED]
    return [c + repr(s) + Style.RESET_ALL for c, s in zip(colors, shapes)]

def main():
    shapes = create_shapes(21)
    for line in format_shapes(shapes):
        print(line)

if __name__ == "__main__":
    main()
