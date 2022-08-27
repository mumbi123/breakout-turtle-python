from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.goto(200, -300)
        self.x_move = 0
        self.y_move = 5
        self.move_speed = 5

    def move(self):

        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1


position = [(-60, -280), (0, -280), (60, -280)]


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_paddle()
        self.x_move = 50
        self.y_move = 50
        print(self.segments)

    def create_paddle(self):
        for pos in position:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.shapesize(stretch_len=3, stretch_wid=1.5)
        new_segment.penup()
        new_segment.color("#A62349")
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def move_right(self):
        for seg in self.segments:
            seg.goto(seg.xcor() + self.x_move, seg.ycor())

    def move_left(self):
        for seg in self.segments:
            seg.goto(seg.xcor() - self.x_move, seg.ycor())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.white_score = 0
        self.color_score = 0
        self.score = 0
        self.penup()
        self.color("#A62349")
        self.hideturtle()
        self.goto(200, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.score = self.white_score + self.color_score
        self.write(f"Score: {self.score}", font=("Arial", 24, "normal"))

    def increase_score_w(self):
        self.white_score += 4
        self.update_scoreboard()

    def increase_score_c(self):
        self.color_score += 7
        self.update_scoreboard()

    def game_over(self):
        self.goto(-280, -150)
        self.write(f"GAME OVER, final score is: {self.score} ", font=("Arial", 36, "normal"))

    def win_game(self):
        self.goto(-280, -150)
        self.write(f"YOU ARE AWESOME, BRAVO", font=("Arial", 36, "normal"))

c_pos = [(-360, 150), (-270, 150), (-180, 150), (-90, 150), (0, 150), (90, 150), (180, 150), (270, 150), (360, 150), (-360, 200), (-270, 200), (-180, 200), (-90, 200), (0, 200), (90, 200), (180, 200), (270, 200), (360, 200)]
w_pos = [(-360, 50), (-270, 50), (-180, 50), (-90, 50), (0, 50), (90, 50), (180, 50), (270, 50), (360, 50), (-360, 100), (-270, 100), (-180, 100), (-90, 100), (0, 100), (90, 100), (180, 100), (270, 100), (360, 100)]


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.color_wall = []
        self.white_wall = []
        self.white_position()
        self.color_position()
        print(self.color_wall)
        print(self.white_wall)

    def white_position(self):
        for data in w_pos:
            new_seg_w = Turtle()
            new_seg_w.shape("square")
            new_seg_w.shapesize(stretch_len=4, stretch_wid=2)
            new_seg_w.color("white")
            new_seg_w.penup()
            new_seg_w.goto(data)
            self.white_wall.append(new_seg_w)

    def color_position(self):
        for data in c_pos:
            new_seg_c = Turtle()
            new_seg_c.shape("square")
            new_seg_c.shapesize(stretch_len=4, stretch_wid=2)
            new_seg_c.color("blue")
            new_seg_c.penup()
            new_seg_c.goto(data)
            self.color_wall.append(new_seg_c)