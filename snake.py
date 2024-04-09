from turtle import Turtle

MYPOSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for positions in MYPOSITIONS:
            self.add_segment(positions)


    def extend(self):
        self.add_segment(self.segment[-1].position())

    def add_segment(self, positions):
        newsegment = Turtle('square')
        newsegment.color('white')
        newsegment.penup()
        newsegment.goto(positions)
        self.segment.append(newsegment)

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            newX = self.segment[seg - 1].xcor()
            newY = self.segment[seg - 1].ycor()
            self.segment[seg].goto(newX, newY)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
