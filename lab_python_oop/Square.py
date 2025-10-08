from .Rectangle import Rectangle

class Square(Rectangle):
    name = "Квадрат"

    def __init__(self, side: float, color: str):
        super().__init__(side, side, color)

    def __repr__(self) -> str:
        return ("{name}: Сторона={side}, Цвет={color}, "
                "Площадь={area:.2f}").format(
                    name=self.name(),
                    side=self.width,
                    color=str(self.color),
                    area=self.area()
                )
