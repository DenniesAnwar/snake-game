from turtle import Turtle, Screen
import time

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[2]
        self.size_of_snake = len(self.segments)


    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)


    def add_segment(self):
        x_cor = self.tail.xcor()
        y_cor = self.tail.ycor()
        tail_pos = (x_cor,y_cor)
        new_tail = Turtle("square")
        new_tail.penup()
        new_tail.color("white")
        new_tail.goto(tail_pos)
        self.segments.append(new_tail)
        self.tail = self.segments[self.size_of_snake - 1]

    def reset(self):
        # To remove off the screen
        for segments in self.segments:
            segments.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)


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


