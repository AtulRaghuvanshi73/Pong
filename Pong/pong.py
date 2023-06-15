#Simple pong game 
import turtle
#import os [import to make this program work on mac and linux and comment out the winsound use cases]
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


#score count 
score_a = 0
score_b = 0

#left paddle 
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid = 5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)

#right paddle 

paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid = 5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350,0)


#pong_ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1


#displaying scores
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
#printing the scores : 
pen.write("Player A:0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Functions
def paddle_left_up():
    y = paddle_left.ycor()#to get the Y-Coordinates
    y+= 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()#to get the Y-Coordinates
    y-= 20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()#to get the Y-Coordinates
    y+= 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()#to get the Y-Coordinates
    y-= 20
    paddle_right.sety(y)

#keyboard binding
wn.listen()

# key binding for the left paddle
wn.onkeypress(paddle_left_up,"w")
wn.onkeypress(paddle_left_down,"s")

#key binding for the right paddle 
wn.onkeypress(paddle_right_up,"i")
wn.onkeypress(paddle_right_down,"k")

#Main game loop 
while True:
    wn.update()

    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("afplay bounce.wav&") 
        # here, use afplay for Mac, aplay for Linux
        """
            to make the same thing work in windows we have to import winsound 
        """
        


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("afplay bounce.wav&") 
        # here, use afplay for Mac, aplay for Linux

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        #printing the scores while updating them 
        pen.write("Player A:{}  Player B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        #printing the scores while updating them 
        pen.write("Player A:{}  Player B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("afplay bounce.wav&") 
        # here, use afplay for Mac, aplay for Linux

    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("afplay bounce.wav&") 
        # here, use afplay for Mac, aplay for Linux
    