import math
from .GeometricFigure import GeometricFigure
from .Color import Color

class Circle(GeometricFigure):
    name = "Круг"

    def __init__(self, radius: float, color: str):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = float(radius)
        self.color = Color(color)

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    @classmethod
    def get_name(cls) -> str:
        return cls.name

    def __repr__(self) -> str:
        return "{name} цвета: {color} радиус={radius}, площадь={area:.2f}".format(
            name=self.get_name(),
            color=self.color,
            radius=self.radius,
            area=self.area()
        )
