import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(560,565)

tina.speed(0)

def fractal_triangle(size,depth):
    if depth == 0: #base case, draw a triangle
        tina.begin_fill()
        for i in range(3):
            tina.forward(size)
            tina.left(120)
        tina.end_fill()
    else: #recursive case, draw 3 smaller fractals
        for i in range(3):
            fractal_triangle(size/2,depth-1)
            tina.forward(size)
            tina.left(120)

#move tina to a good start spot
tina.penup()
tina.goto(-275,-275)
tina.pendown()
#draw the fractal
fractal_triangle(550,4)

turtle.exitonclick()