from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square


from colorama import Fore, Style, init

def main():
    N = 21
    rect = Rectangle(N, N, "синий")
    circ = Circle(N, "зеленый")
    sq = Square(N, "красный")

    init(autoreset=True)

    print(Fore.BLUE + repr(rect) + Style.RESET_ALL)
    print(Fore.GREEN + repr(circ) + Style.RESET_ALL)
    print(Fore.RED + repr(sq) + Style.RESET_ALL)

if __name__ == "__main__":
    main()
