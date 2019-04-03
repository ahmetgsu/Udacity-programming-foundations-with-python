import turtle

def draw_square(some_turtle):
    some_turtle.speed(11)
    some_turtle.left(30)
    some_turtle.forward(100)
    some_turtle.left(90)
    some_turtle.forward(100*(3**(1.0/2)))
    some_turtle.left(120)
    some_turtle.forward(100*(3**(1.0/2)))
    some_turtle.left(90)
    some_turtle.forward(100)
                          
def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    #create the turtle brad
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("purple")
    brad.speed(11)
    for i in range(1,73):
        draw_square(brad)
        brad.right(5)

    window.exitonclick()

draw_art()
