import turtle

turtle.Turtle() # Declaring Turtle Class
turtle.speed(1) # Controlling speed(lowest)

turtle.pencolor('blue')

for i in range(3):
	turtle.forward(100)
	turtle.left(120)

turtle.exitonclick()
