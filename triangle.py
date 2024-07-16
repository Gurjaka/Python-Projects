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
            return False
        return False

side1 = int(input("Side1: "))
base = int(input("base: "))
side2 = int(input("Side2: "))

triangle = TriangleChecker([side1, base, side2])
if triangle.is_triangle():
    tria = [side1,base,side2]
    tria.sort()
    height = (tria[0]*tria[1])/tria[2]
    area = (base*height)/2
    ball_size = int(input("Ball size in cm: "))    
    ball = math.pi*(ball_size/2)**2
    ball_quantity = area/ball
    print(ball_quantity)
