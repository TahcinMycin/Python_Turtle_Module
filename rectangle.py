import turtle

turtle.Turtle() # Declaring Turtle Class
turtle.speed(1) # Controlling speed(lowest)

for i in range(4):
	turtle.forward(100)
	turtle.left(90)

turtle.exitonclick()
