import turtle
import math

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(560,565)

tina.speed(0)

def fractal_hex(size,depth):
  if(depth == 0): # base case
    tina.left(30)
    tina.forward(size)
    tina.right(120)
    tina.begin_fill()
    for i in range(6):
      tina.forward(size)
      tina.right(60)
    tina.end_fill()
    tina.right(60)
    tina.forward(size)
    tina.left(150)
  else: # recursive case
    #move to center of first hex to draw
    tina.penup()
    tina.forward(size/math.sqrt(3))
    tina.pendown()
    
    tina.right(120)
    for i in range(6):
      fractal_hex(size/3,depth-1)
      tina.penup()
      tina.forward(size/math.sqrt(3))
      tina.pendown()
      tina.right(60)
    tina.left(120)
    tina.penup()
    tina.backward(size/math.sqrt(3))
    tina.pendown()


def fractal_square(size,depth):
  if(depth == 0): # base case
    tina.begin_fill()
    for i in range(4):
      tina.forward(size)
      tina.right(90)
    tina.end_fill()
  else: # recursive case
    for i in range(4):
      fractal_square(size / 3.0, depth-1)
      tina.forward(size/3.0)
      fractal_square(size / 3.0, depth-1)
      tina.forward(size*2/3.0)
      tina.right(90)


def fractal_curve(size, depth):
    if depth == 0: #draw a 2 right angles
        tina.forward(size)
        tina.left(90)
        tina.forward(size)
        tina.



def fractal_triangle(size,depth):
    if depth == 0: #base case, draw a triangle
        #tina.begin_fill()
        for i in range(3):
            tina.forward(size)
            tina.left(120)
        #tina.end_fill()
    else: #recursive case, draw 3 smaller fractals
        for i in range(3):
            fractal_triangle(size/2,depth-1)
            tina.forward(size)
            tina.left(120)

#move tina to a good start spot
tina.penup()
#tina.goto(-275,-275)
tina.left(90)
tina.pendown()
#draw the fractal
fractal_hex(275,4)

turtle.exitonclick()