import math

from gameLib import *

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    def direction(self, other):
        return (other - self) / self.distance(other)
    
    def lerp(self, other, t):
        return self + (other - self) * t

    def as_tuple(self):
        return (self.x, self.y)

    def copy(self):
        return Vector(self.x, self.y)
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)
    
    def __div__(self, other):
        return Vector(self.x / other, self.y / other)