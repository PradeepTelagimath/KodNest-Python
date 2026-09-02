class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side


length, breadth, side = map(int, input().split())

shapes = [Rectangle(length, breadth), Square(side)]

for shape in shapes:
    print(shape.perimeter())