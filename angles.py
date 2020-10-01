import turtle     # importing the module
import time    #importing the time module trtl = turtle.Turtle()     #making a turtle object of Turtle class for drawing
screen=turtle.Screen()     #making a canvas for drawing
screen.setup(620,470)     #choosing the screen size
screen.bgpic('bg.gif')     #making canvas black
trtl.pencolor('red')     #making colour of the pen red
trtl.pensize(5)     #choosing the size of pen nib
trtl.speed(1)     #choosing the speed of drawing
trtl.shape('turtle')    #choosing the shape of pen nib
time.sleep(12)
n=3    starting for a triangle
shapes=['Triangle','Square','Pentagon','Hexagon','Heptagon','Octagon','Nonagon','Decagon']
while n<11: #    limiting to a decagon
        for i in range(n):     # for loop to minimize the same lines of codes being written
            trtl.pencolor('red')
            trtl.forward(100)     #top line
            trtl.right(360/n)    #determining the exterior angle of the polygon
trtl.penup()
trtl.setpos(-80,180)    #moving the turtle to make the animation more centric
trtl.pendown()
trtl.pencolor('blue')
trtl.write(' This is '+shapes[n-3], font=("Arial", 16, "bold"))    #printing the name of the polygon
n=n+1
time.sleep(1)
    #making turtle sleep for one second trtl.clear()
trtl.penup()
trtl.setpos(-n*8,n*14)
trtl.pendown
