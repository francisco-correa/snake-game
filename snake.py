import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0
body = []

screen = turtle.Screen()
screen.title("The Snake Game by Francisco Correa")
screen.bgcolor("#FFFACD")
screen.setup(width=500, height=500)
screen.tracer(0)

snake = turtle.Turtle()
snake.color("#008B8B")
snake.shape("square")
snake.penup()
snake.speed(0)
snake.goto(0,0)
snake.direction = "stop"

food = turtle.Turtle()
food.color("#DC143C")
food.shape("circle")
food.penup()
food.goto(50,50)

points = turtle.Turtle()
points.color("#00008B")
points.hideturtle()
points.penup()
points.goto(0,220)
points.write("Your Score: 0  High Score: 0", font=("Times New Roman", 20), align="center")

def go_up():
    if snake.direction != "down":
        snake.direction = "up"
def go_down():
    if snake.direction != "up":
        snake.direction = "down"
def go_right():
    if snake.direction != "left":
        snake.direction = "right"
def go_left():
    if snake.direction != "right":
        snake.direction = "left"
def moveSnake():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 10)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 10)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 10)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 10)

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_left, "Left")

while True:
    screen.update()
    if snake.xcor() > 240 or snake.xcor() < -240 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "stop"

        for x in body:
            x.goto(800, 800)
        body.clear()
        
        delay = 0.1
        score = 0
        points.clear()
        points.write("Your Score: {}  High Score: {}".format(score, high_score), font=("Times New Roman", 20), align="center")

    if snake.distance(food) < 10:
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        food.goto(x, y)
    
        new_body = turtle.Turtle()
        new_body.shape("square")
        new_body.color("grey")
        new_body.speed(0)
        new_body.penup()
        body.append(new_body)

        delay -= 0.0009
        score += 1
        if score > high_score:
            high_score = score
        points.clear()
        points.write("Your Score: {}  High Score: {}".format(score, high_score), font=("Times New Roman", 20), align="center")
    
    for i in range(len(body)-1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)
    
    if len(body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)
    moveSnake()

    for x in body:
        if x.distance(snake) < 10:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"

            for x in body:
                x.goto(800, 800)
            body.clear()

            delay = 0.1
            score = 0
            points.clear()
            points.write("Your Score: {}  High Score: {}   ".format(score, high_score), font=("Times New Roman", 20), align="center")

    time.sleep(delay)
screen.mainloop() 