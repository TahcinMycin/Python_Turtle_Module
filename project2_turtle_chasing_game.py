import turtle
from helpercode import checkpos, intersect, Counter
import random

screen = turtle.Screen()
screen.setworldcoordinates(-400,-400,400,400)

class Runner(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape('turtle')
    self.penup()
    screen.tracer(10)
    self.setpos(-100,0)
    self.seth(0)
    self.pendown()
    screen.tracer(1)
  def reset(self):
    self.hideturtle()
    self.clear()
    self.__init__()

# A list of all of our chasers
chasers = []

class Chaser(turtle.Turtle):
  def __init__(self, target, coordinates = [100,0]):
    turtle.Turtle.__init__(self)
    self.target = target
    self.start = coordinates
    self.shape('turtle')
    c1 = abs(coordinates[0])
    c2 = abs(coordinates[1])
    c3 = max(255, abs(sum(coordinates)))
    self.color(c1, c2, c3)
    self.penup()
    screen.tracer(0)
    self.setpos(self.start)
    self.seth(self.towards(target))
    self.pendown()
    screen.tracer(1)
    # Add Self to list of Chasers
    chasers.append(self)
  
  def reset(self):
    self.hideturtle()
    self.clear()
    self.__init__(self.target)
  
  def track(self, move=False):
    screen.tracer(0)
    self.seth(self.towards(self.target) + random.randint(-25,25))
    self.width(self.distance(self.target.pos()) //20)
    if intersect(self.target,self):
      x,y = self.pos()
      c1 = abs(x)
      c2 = abs(y)
      c3 = max(256, abs(sum([x,y])))
      self.color((c1, c2, c3))
      self.penup()
      self.goto(self.start)
      self.pendown()
    elif move:
      self.forward(9+random.randint(-4,0))
    else:
      self.forward(1)
    checkpos([self.target,self],screen)
    screen.tracer(1)

main = Runner()
main.write("Click and Drag!")
main.backward(20)
c1 = Chaser(main, [200,-50])
c2 = Chaser(main, [50,200])
johnny = Chaser(main, [-150,-100])

# Reset the game to original state
def reset():
  main.reset()
  c1.reset()

# Define functions for each arrow key
def go_left():
  screen.tracer(0)
  main.left(7)
  c1.track()
  
def go_right():
  screen.tracer(0)
  main.right(7)
  c1.track()
  
def go_forward():
  screen.tracer(0)
  main.forward(10)
  c1.track(move=True)
  
def go_backward():
  screen.tracer(0)
  main.backward(10)
  c1.track(move=True)
  
# Tell the program which functions go with which keys
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')
screen.onkey(go_forward, 'Up')
screen.onkey(go_backward, 'Down')

def drag_function(x,y):
  screen.tracer(0)
  main.clear()
  main.goto(x,y)
  for chaser in chasers:
    chaser.track(True)
  screen.tracer(1)

main.ondrag(drag_function)

# Reset the game when the user presses 'r'
screen.onkey(reset,"r")

# Tell the screen to listen for key presses
screen.listen()
turtle.done()
