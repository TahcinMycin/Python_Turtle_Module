import turtle

counterscreen = turtle.Screen()
counterscreen.bgcolor("palegoldenrod")

def checkpos(turtlelist, screen):
  """
  Takes a list of turtle objects and a Screen object.
  Sets the turtles to the opposite edge of the screen.
  """
  screen.tracer(0)
  for turtle in turtlelist:
    dim = 400
    turtle.penup()
    x = turtle.xcor()
    y = turtle.ycor()
    if x > dim:
      turtle.setx(-1 * dim)
    elif x < -1 * dim:
      turtle.setx(dim)
    if y > dim:
      turtle.sety(-1* dim)
    elif y < -1 * dim:
      turtle.sety(dim)
    turtle.pendown()
  screen.tracer(1)
  return

def intersect(object1, object2, radius = 15):
  """
  Takes two Turtle objects and an optional radius.
  Returns True if the objects are less than radius apart.
  """
  xbounds = (object1.xcor()-radius, object1.xcor() + radius)
  ybounds = (object1.ycor()-radius, object1.ycor() + radius)
  x, y = object2.pos()
  check_x = x > min(xbounds) and x < max(xbounds)
  check_y = y > min(ybounds) and y < max(ybounds)
  if (check_x and check_y):
    return True
  else:
    return False
    
class Counter(turtle.Turtle):
  def __init__(self, coordinates = [160, 170], screen = counterscreen):
    turtle.Turtle.__init__(self)
    self.count = 0
    self.hideturtle()
    self.speed(0)
    self.penup()
    self.goto(coordinates)
    self.screen = screen
  def show(self, message, alignment = "right", size = 18):
    self.screen.tracer(0)
    self.clear()
    self.write(message,font=("Arial",size),align=alignment)
    self.screen.tracer(1)
  def increment(self):
    self.count += 1
  def showcount(self, x = 0, y = 0):
    self.increment()
    self.show(self.count)
      
