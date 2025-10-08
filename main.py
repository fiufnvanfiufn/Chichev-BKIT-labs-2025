import sys
from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square

import colorama
from colorama import Fore, Style

def main():
    try:
        N = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    except ValueError:
        print("Аргумент N должен быть целым числом. Используется N=1.")
        N = 1

    rect = Rectangle(N, N, "синий")
    circ = Circle(N, "зеленый")
    sq = Square(N, "красный")

    colorama.init(autoreset=True)

    print(Fore.BLUE + repr(rect) + Style.RESET_ALL)
    print(Fore.GREEN + repr(circ) + Style.RESET_ALL)
    print(Fore.RED + repr(sq) + Style.RESET_ALL)

if __name__ == "__main__":
    main()
