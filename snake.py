import turtle
import random
import time

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
    if snake.distance(food) < 10:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        food.goto(x, y)

    move()
    time.sleep(delay)

# turtle.done()
screen.mainloop() 
# turtle.showTurtle()