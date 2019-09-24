from graphics import *

#Amanda Maglaras
#amanda.maglaras1@marist.edu
#This project required us to build a traffic light using graphics.py in python.
#The rectangle had to have a white backgroud with a black outline.
#All circles had to be the same size in the proper order of a traffic light. 

def main():
    win=GraphWin("Traffic Light")
    rectangle=Rectangle(Point(40, 40), Point(100, 160))
    rectangle.setOutline("black")
    rectangle.setFill("white")
    rectangle.draw(win)
    
    redlight=Circle(Point(70, 65), 16)
    redlight.setOutline("black")
    redlight.setFill("red")
    redlight.draw(win)
    
    yellowlight=Circle(Point(70, 100), 16)
    yellowlight.setOutline("black")
    yellowlight.setFill("yellow")
    yellowlight.draw(win)
    
    greenlight=Circle(Point(70, 135), 16)
    greenlight.setOutline("black")
    greenlight.setFill("green")
    greenlight.draw(win)



main()
    
    



