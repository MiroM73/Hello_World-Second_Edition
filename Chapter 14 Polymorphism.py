# Here is a triengle class
class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # Triangle and Square have a method called getArea() with different calculations
    # This is called polymorphism, differend classes has the methods with same name
    def getArea(self):
        area = self.width * self.height / 2.0
        return area

# Here is a square class
class Square:
    def __init__(self, size):
        self.size = size
    # Triangle and Square have a method called getArea() with different calculations
    # This is called polymorphism, differend classes has the methods with same name
    def getArea(self):
        area = self.size * self.size
        return area

myTriangle = Triangle(4, 5)
mySquare = Square(7)

print myTriangle.getArea()
print mySquare.getArea()
