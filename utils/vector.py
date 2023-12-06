from dataclasses import dataclass


@dataclass(frozen=True)
class Vector2:
    x: int
    y: int

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
