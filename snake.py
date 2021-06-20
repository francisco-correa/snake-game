import turtle
import time
import random

delay = 0.1
score = 0

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

body = []

def go_up():
    snake.direction = "up"
def go_down():
    snake.direction = "down"
def go_right():
    snake.direction = "right"
def go_left():
    snake.direction = "left"
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 15)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 15)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 15)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 15)

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_left, "Left")

while True:
    screen.update()
    if snake.xcor() > 250 or snake.xcor() < -250 or snake.ycor() > 250 or snake.ycor() < -250:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "stop"

        for x in body:
            x.goto(1000, 1000)
        body.clear()

    if snake.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)
    
        new_body = turtle.Turtle()
        new_body.shape("square")
        new_body.color("grey")
        new_body.speed(0)
        new_body.penup()
        body.append(new_body)
    
    for i in range(len(body)-1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)
    
    if len(body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)
    move()

    # for x in body:
    #     if x.distance(body) < 20:
    #         time.sleep(1)
    #         snake.goto(0,0)
    #         snake.direction = "stop"

    #         for x in body:
    #             x.goto(1000, 1000)
    #         body.clear()

    time.sleep(delay)

# turtle.done()
screen.mainloop() 
# turtle.showTurtle()