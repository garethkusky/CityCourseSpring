__author__ = 'acpb968'
#Following the example of the Circle class seen in the course, design a class named Rectangle
#to represent a rectangle. The class contains:
# Two data fields named width and height.
# A constructor that creates a rectangle with the specified width and height.
# The default values are 1 and 2 for the width and height, respectively.
# A method named getArea()that returns the area of this rectangle.
# A method named getPerimeter()that returns the perimeter.
# Draw the UML diagram for the class, and then implement the class. Write a test program that
# creates two Rectangle objects—one with width 4 and height 40 and the other with width 3.5 and
# height 35.7. Display the width, height, area, and perimeter of each rectangle in this order

import math
class rectangle:
    # Construct a rectangle object with default sizes
    def __init__(self, width = 1, height=2):
        self.width = width
        self.height=height

    def getPerimeter(self):
        return (self.width *2) + (self.height *2)

    def getArea(self):
        return self.width * self.height

    def setRadius(self, width, height):
        self.width = width
        self.height=height
