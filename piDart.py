# piDart.py
# author: Renata Paramastri
# June 2016

import turtle
import random
import time

RANDOM_COLOR = "black"
MANUAL_COLOR = "gold"

def main():
    board = Board()
    board.drawBoard()
    turtle.onscreenclick(board.userThrow)

    return board

class Board(object):
    def __init__(self, radius = 350, dartSize = 10):
        self.circleDarts = 0
        self.totalDarts = 0
        self.radius = radius
        self.dartSize = dartSize

    def estimatePi(self):
        return self.circleDarts / self.totalDarts * 4

    def evaluateThrow(self, x,y):
        """ Increments the number of darts in the circle
        if a dart was thrown in the circle
        """
        if x**2 + y**2 < self.radius**2:
            self.circleDarts += 1

    def randomThrow(self, numDarts = 1):
        """ Returns a tuple (x,y)
        where (x,y) is a random location within the square.
        Draws a dot where the dart was thrown.
        """
        self.totalDarts += numDarts
        for i in range(numDarts):
            # + 1 since uniform returns in the range
            x = random.uniform(-(self.radius + 1), self.radius + 1) 
            y = random.uniform(-(self.radius + 1), self.radius + 1) 
            
            self.drawDart(x,y, random=True)
            self.evaluateThrow(x,y)
            time.sleep(0.25)  # to follow along with the throws

    def userThrow(self, x,y):
        """ Lets the user click on the screen to throw a dart.
        Returns true if they clicked in the circle. """
        if x in range(-self.radius, self.radius) and \
           y in range(-self.radius, self.radius):
            self.drawDart(x,y,random=False)
            self.totalDarts += 1
            self.evaluateThrow(x,y)

        else:
            print("Click in the square!")


    def drawDart(self, x, y, random):
        """ Draws a dot in the given coordinates.
        random -- boolean, dictates color of dart.
        Note: assumes that (x,y) is within the square.
        """
        turtle.speed(0)
        turtle.penup()
        turtle.setposition(x,y)
        if random:
            turtle.dot(self.dartSize, RANDOM_COLOR)
        else:
            turtle.dot(self.dartSize, MANUAL_COLOR)

    def drawBoard(self):
        """ Draws the circle and the square."""
        turtle.reset()          # ensures that turtle is at the origin
        turtle.shape("turtle")  # greatly improves the experience
        turtle.penup()
        turtle.forward(self.radius) # make (0,0) the center of the board

        # draw square
        turtle.pendown()
        turtle.left(90)
        turtle.forward(self.radius)      # top half of right side
        turtle.left(90)
        turtle.forward(self.radius * 2)  # top
        turtle.left(90)
        turtle.forward(self.radius * 2)  # left
        turtle.left(90)
        turtle.forward(self.radius * 2)  # bottom
        turtle.left(90)
        turtle.forward(self.radius)      # lower half of right side

        # draw circle
        turtle.circle(self.radius)
        turtle.hideturtle()
