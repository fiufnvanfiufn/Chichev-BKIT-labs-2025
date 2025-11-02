import unittest
from lab_python_oop.Rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def testArea(self):
        rectangle = Rectangle(3, 4, "синий")
        self.assertEqual(rectangle.area(), 12)

    def testColor(self):
        rect = Rectangle(3, 4, "красный")
        self.assertEqual(str(rect.color), "красный")

    def testRepr(self):
        rectangle = Rectangle(3, 4, "красный")
        reprString = repr(rectangle)
        self.assertIn("красный", reprString)
        self.assertIn("Прямоугольник", reprString)


if __name__ == "__main__":
    unittest.main()
