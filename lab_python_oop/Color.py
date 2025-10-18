class Color:
    def __init__(self, color_value: str):
        self.color_value = color_value

    def __str__(self) -> str:
        return self.color_value

    def __repr__(self) -> str:
        return f"Color('{self.color_value}')"
