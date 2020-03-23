#Building a Pong Game

#Import Turtle module which is like a drawing board.
import turtle

#Create a window screen.

window = turtle.Screen()

#Name the window screen.

window.title("Pong Game")

#Make the background color of the screen black.

window.bgcolor("black")

#Adjust the width and height of the screen.

window.setup(width=800, height=600)

#Stop the window from updating so that it can speed up the game. Otherwise, the game would run much slower.

window.tracer(0)


#Create score.

score_a = 0

score_b = 0



#Create Paddles and Ball. 

#Paddle 1.

#Capital Turtle is the class of the module.

paddle_1 = turtle.Turtle()

#Set the speed of the animation not how the paddle moves on the screen. Sets the speed to the maximum speed otherwise everything will run slow.

paddle_1.speed(0)

#Give the paddle a shape. There are several built in shapes including "square".

paddle_1.shape("square")

#Give the paddle a color.

paddle_1.color("white")


#By default the pixels are 20px by 20px. Here we are going to stretch the shape of the paddle by 5 for the width which is "5px X 20px = 100px". We keep the length the same (20px).

paddle_1.shapesize(stretch_wid=5, stretch_len=1)


#Turtle module usually draws a line as we are moving so we use "penup" so that does not occur.

paddle_1.penup()

#Create the starting point of my paddle on the left side of the screen hence the (-) sign.

paddle_1.goto(-350, 0)



#Paddle 2.

paddle_2 = turtle.Turtle()

#Set the speed of the animation not how the paddle moves on the screen. Sets the speed to the maximum speed otherwise everything will run slow.

paddle_2.speed(0)

#Give the paddle a shape. There are several built in shapes including "square".

paddle_2.shape("square")

#Give the paddle a color.

paddle_2.color("white")


#By default the pixels are 20px by 20px. Here we are going to stretch the shape of the paddle by 5 for the width which is "5px X 20px = 100px". We keep the length the same (20px).

paddle_2.shapesize(stretch_wid=5, stretch_len=1)


#Turtle module usually draws a line as we are moving so we use "penup" so that does not occur.

paddle_2.penup()

#Create the starting point of my paddle on the right side of the screen.

paddle_2.goto(350, 0)



#Ball.

ball = turtle.Turtle()

#Set the speed of the animation not how the ball moves on the screen. 

ball.speed(0)

#Give the ball a shape. 

ball.shape("circle")

#Give the ball a color.

ball.color("white")

#Turtle module usually draws a line as we are moving so we use "penup" so that does not occur.

ball.penup()

#Create the starting point of the ball in the middle of the screen.

ball.goto(0, 0)

#Moving the ball.
#We are going to use "dx". "d" means delta or change. Every time the ball moves it moves by px on x and y axis. 

ball.dx = 1
ball.dy = -1



#Create pen or scorecard.

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))


#Here we are going to create several functions in order to move the paddles on the screen.

#Create a function to move paddle 1 up.

#Define the function.
def paddle_1_up():
	#Here we need to know the current coordinates of the y axis. "ycor" from the turtle module and returns the y coordinate.
	y = paddle_1.ycor()

	#Add 20px to y so that it can go up.
	y += 20

	#Now, we have to set y to the new calculation.

	paddle_1.sety(y)


def paddle_1_down():
	#Here we need to know the current coordinates of the y axis. "ycor" from the turtle module and returns the y coordinate.
	y = paddle_1.ycor()

	#Subtract 20px to y so that it can go down.
	y -= 20

	#Now, we have to set y to the new calculation.

	paddle_1.sety(y)


# Paddle 2 Functions.

def paddle_2_up():
	#Here we need to know the current coordinates of the y axis. "ycor" from the turtle module and returns the y coordinate.
	y = paddle_2.ycor()

	#Add 20px to y so that it can go up.
	y += 20

	#Now, we have to set y to the new calculation.

	paddle_2.sety(y)


def paddle_2_down():
	#Here we need to know the current coordinates of the y axis. "ycor" from the turtle module and returns the y coordinate.
	y = paddle_2.ycor()

	#Subtract 20px to y so that it can go down.
	y -= 20

	#Now, we have to set y to the new calculation.

	paddle_2.sety(y)

#Keyboard binding to call the function.

#We use "listen" from the turtle module so that it can listen for keyboard input.

window.listen()

#When the user presses the "s" key to call the function "paddle_1_up" and the "x" key for "paddle_1_down".

window.onkeypress(paddle_1_up, "s")
window.onkeypress(paddle_1_down, "x")

#When the user presses the "Up" arrow key to call the function "paddle_2_up" and the "Down" arrow key for "paddle_2_down".

window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")


#Main game loop.

while True:
	#Eveytime the loop runs it updates the screen.
	window.update()

	#Move the ball. Ball starts at "0,0" but moves "1,1" with this command and moves diagonally.

	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Border checking. Stop the ball from going off the screen.
	#Here we originally set the screen height to 600 and if we half that (300) and then use 290 so that is the border. "-1" is the change to the delta. The ball's direction should reverse.
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1


	if ball.ycor() > -290:
		ball.sety(-290)
		ball.dy *= -1

	#Here we originally set the screen width to 800 and if we half that (400) and then use 390 so that is the border. 

	if ball.xcor() > 390:
		#If ball goes pass paddle, put the ball back in the center.
		ball.goto(0,0)
		#Then we have the ball reverse direction.
		ball.dx *= -1
		score_a += 1
		#Clears score.
		pen.clear()
		#Increments players scores.
		pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


	if ball.xcor() < -390:
		#If ball goes pass paddle, put the ball back in the center.
		ball.goto(0,0)
		#Then we have the ball reverse direction.
		ball.dx *= -1
		score_b += 1
		#Clears score.
		pen.clear()
		#Increments players scores.
		pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


	#Paddle and ball collisions. The edges are touching and if the ball is between the size of the paddle

	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 50):
		#Moves back to the left a little bit.
		ball.setx(340)
		ball.dx *= -1

	if (ball.xcor() > -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 50):
		#Moves back to the left a little bit.
		ball.setx(-340)
		ball.dx *= -1


