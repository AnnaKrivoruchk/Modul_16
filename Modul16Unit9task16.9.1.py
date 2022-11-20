class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}.'

rect_1 = Rectangle(5, 10, 50, 100)
rect_2 = Rectangle(10, 20, 40, 200)

print(rect_1)
print(rect_2)

