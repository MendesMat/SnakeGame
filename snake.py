from turtle import Turtle


class Snake:

    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVEMENT_SPEED = 20

    def __init__(self):
        self.snake_segments = []
        self.create_initial_snake()
        self.head = self.snake_segments[0]

    def create_initial_snake(self):
        for index in self.STARTING_POSITIONS:
            self.add_segment()

    def add_segment(self):
        new_snake_part = Turtle(shape="square")
        new_snake_part.penup()
        new_snake_part.color("green")
        self.snake_segments.append(new_snake_part)

    def movement_behaviour(self):
        # Runs the segments list backwards
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            # Stores the position of the next segment
            next_seg_pos = self.snake_segments[seg_num - 1].pos()
            # Makes the before segment follow the position of its next segment
            self.snake_segments[seg_num].goto(next_seg_pos)

        # Moves the snake head forward
        self.snake_segments[0].forward(self.MOVEMENT_SPEED)

    def set_heading(self, direction):
        current_heading = self.head.heading()
        # Makes so the snake can't turn the opposite direction
        if abs(direction - current_heading) != 180:
            self.head.setheading(direction)
