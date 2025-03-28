import turtle


turtle.setup(width=600, height=400)
turtle.bgcolor("white")
turtle.speed(5)  

def draw_ring(color, x, y):
    turtle.penup()
    turtle.goto(x, y)  
    turtle.pendown()
    turtle.pensize(8)
    turtle.pencolor(color)
    turtle.circle(70)  


draw_ring("blue", -150, 0)   
draw_ring("black", 0, 0)     
draw_ring("red", 150, 0)       
draw_ring("yellow", -75, -80)  
draw_ring("green", 75, -80)   


turtle.hideturtle()
turtle.done()