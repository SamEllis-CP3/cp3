#polymorphism Functions, or methods can do mutipul things based on gven inputs

"""
print(len("geeks"))

print(len([10,20,30]))
"""
import math

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, x):
        self.x = x
    @abstractmethod
    def area(self):
        return 0
    
class Square(Shape):
    def area(self):
        return self.x ** 2
    
class Circle(Shape):
    def area(self):
        return round((self.x ** 2) * math.pi, 2)
    
class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def area(self):
        return self.x * self.y
    
shape = Shape(6)
print(shape.area())

sqr = Square(4)
print(sqr.area())

cir = Circle(4)
print(cir.area())

rec = Rectangle(4,5)
print(rec.area())