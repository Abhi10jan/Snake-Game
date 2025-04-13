STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

from turtle import  Turtle
class Snake:

    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head = self.segment[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def  move(self):
         for i in range(len(self.segment)-1,0,-1):
            position_x = self.segment[i-1].xcor()
            position_y = self.segment[i-1].ycor()
            self.segment[i].goto(position_x, position_y)

         self.head.forward(MOVE_DISTANCE)
    def left(self):
       if self.head.heading()!= RIGHT:
         self.head.setheading(180)


    def  right(self):
        if self.head.heading() != LEFT:
          self.head.setheading(0)

    def up(self):
        if self.head.heading() !=DOWN:
          self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
          self.head.setheading(270)
