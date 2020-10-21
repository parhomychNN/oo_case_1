from __future__ import annotations

from math import sqrt


class Point(object):
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_distance_to(self, another: Point) -> float:
        return sqrt((another.x - self.x) ** 2 + (another.y - self.y) ** 2)

    def __str__(self):
        return "Point: x = " + str(self.x) + ", y = " + str(self.y)
