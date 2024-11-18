import math

class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return True
        return False

    def calculate_area(self):
        if self.is_triangle():
            a, b, c = self.sides
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            return area
        return None

side1 = int(input("Side1: "))
base = int(input("Base: "))
side2 = int(input("Side2: "))
triangle = TriangleChecker([side1, base, side2])

if triangle.is_triangle():
    area = triangle.calculate_area()
    print(f"Triangle area: {area:.2f} square cm")
    ball_size = int(input("Ball size in cm (diameter): "))
    radius = ball_size / 2
    ball_area = math.pi * (radius ** 2)
    ball_quantity = area / ball_area
    print(f"Number of balls that can fit: {int(ball_quantity)}")
else:
    print("The given sides do not form a triangle.")
