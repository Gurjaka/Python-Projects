class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides
    
    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return "Yay, This is a triangle!"
                return ":( This is not a triangle!"
            return "Only use positive Integers!"
        return "The input must be Integers!"
    
# Checkers
triangle1 = TriangleChecker([2,3,4])
print(triangle1.is_triangle())
triangle2 = TriangleChecker([77,3,4])
print(triangle2.is_triangle())
triangle3 = TriangleChecker([77,3,"KALBASI"])
print(triangle3.is_triangle())
triangle4 = TriangleChecker([77, -3, 4])
print(triangle4.is_triangle())