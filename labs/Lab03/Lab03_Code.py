
# 1.) open text file

file = open(r"shape.txt")
lines = file.readlines()
file.close()

for line in lines:
    components = line.split(",")
    shape = components[0]
    print("Shape:" + shape)

# 2.) Create a class for each shape found in the text file

    # parent class
class Shape():
    def __init__(self):
        pass
    def getArea(self):
        pass

    # child class (triangle)
class Triangle(Shape):
    def __init__(self, b, h):
        super().__init__()
        self.b = b
        self.h = h
    def getArea(self):
        return 0.5 * self.b * self.h

    # child class (circle)
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def getArea(self):
        return 3.14 * self.radius * self.radius
    
    # child class (rectangle)
class Rectangle(Shape):
    def __init__(self, l, w):
        super().__init__()
        self.l = l
        self.w = w
    def getArea(self):
        return self.l * self.w
    
# 3.) For each line, create a new object determined by the shape

totalShapes = []

for line in line:
    components = line.split(",")
    shape = components[0]
    
    if shape == "Rectangle":
        x = float(components[1])
        y = float(components[2])
        totalShapes.append(Rectangle(x, y))
    elif shape == "Triangle":
        x = float(components[1])
        y = float(components[2])
        totalShapes.append(Rectangle(x, y))
    elif shape == "Circle":
        x = float(components[1])
        totalShapes.append(Circle(x, y))  

# 4.) Iterate through your list and print out the area for each shape

for shape in totalShapes:
    print(shape.getArea())

    

