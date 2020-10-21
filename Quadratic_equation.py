from math import sqrt


class Result_quad_equation(object):
    status: str
    x1: float
    x2: float

    def __init__(self, status, x1, x2):
        self.status = status
        self.x1 = x1
        self.x2 = x2

    def __str__(self):
        return "Status: " + self.status + ", x1 = " + str(self.x1) + ", x2 = " + str(self.x2)


class Quadratic_equation:
    a: float
    b: float
    c: float

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def solve_quad_equation(self) -> Result_quad_equation:
        a = self.a
        b = self.b
        c = self.c
        d = round(b ** 2 - 4 * a * c, 4)
        status: str
        if d < 0:
            status = "No roots"
            return Result_quad_equation(status, None, None)
        elif d == 0:
            status = "1 root"
            x1 = -b / 2 * a
            return Result_quad_equation(status, x1, None)
        else:
            status = "2 roots"
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            return Result_quad_equation(status, x1, x2)
