import turtle

def single_triangle(triangle):
    triangle.begin_fill()
    for i in range(3):
        triangle.left(120)
        triangle.forward(50)
        if i == 0:
            b = triangle.pos()
    triangle.end_fill()
    triangle.setpos(b)

def fractals_1(triangle): #draws the edges of triangle
    a = None
    b = None 
    for i in range(12):
        triangle.begin_fill()
        triangle.left(120)
        triangle.forward(50)
        a = triangle.pos()
        print a
        triangle.left(120)
        triangle.forward(50)
        triangle.right(120)
        triangle.forward(50)
        triangle.left(120)
        triangle.forward(50)
        triangle.left(120)
        triangle.forward(100)
        triangle.end_fill()
        triangle.setpos(a)
        single_triangle(triangle)
        if i == 3:
            triangle.left(120)
        if i == 7:
            triangle.left(120)

def draw_fractals():
    window = turtle.Screen()
    window.bgcolor("white")
    triangle = turtle.Turtle()
    triangle.speed(12)
    triangle.pensize(3)
    triangle.color("red","green")
    fractals_1(triangle)

#    _triangle(triangle)
    window.exitonclick()

draw_fractals()
    
