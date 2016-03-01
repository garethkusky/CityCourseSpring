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

class main():
    rec1=rectangle(4,40)
    rec2=rectangle(3.5,35.7)
    print("rectangle 1: width is ", str(int(rec1.width*100)/100)," Height is ",str(int(rec1.height*100)/100),\
        " Area is ", str(int(rec1.getArea()*100)/100), " Permimiter is ", str(int(rec1.getPerimeter()*100)/100))
    print("rectangle 2: width is ", str(int(rec2.width*100)/100)," Height is ",str(int(rec2.height*100)/100),\
        " Area is ", str(int(rec2.getArea()*100)/100), " Permimiter is ", str(int(rec2.getPerimeter()*100)/100))


main()