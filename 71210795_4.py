from turtle import *

speed(0)

# Grass
bgcolor("green")

# Sky
penup()
goto(-400, -100)
pendown()
color("deepskyblue")
begin_fill()
for i in range(2):
    forward(800)
    left(90)
    forward(500)
    left(90)
end_fill()



penup()
goto(220, 240)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(230, 215)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(180, 225)
pendown()
begin_fill()
circle(25)
end_fill()

# rumah
penup()
goto(-100, -100)
pendown()
pensize(3)
color("chocolate", "blue")  
begin_fill()
for i in range(4):
    forward(170)
    left(90)
end_fill()



# Roof
penup()
goto(-127, 70)
pendown()
begin_fill()
for i in range(3):
    forward(225)
    left(120)
end_fill()

# jendela 1
penup()
goto(0, 0)
pendown()
color("black", "white")
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

# jendela 1  
penup()
goto(0, 25)
pendown()
color("black")
forward(50)

# jendela 1   
penup()
goto(25, 0)
pendown()
left(90)
forward(50)

# jendela 2
penup()
goto(-80, 0)
pendown()
right(90)
color("black", "white")
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

# jendela 2   
penup()
goto(-80, 25)
pendown()
color("black")
forward(50)

# jendela 2  
penup()
goto(-55, 0)
pendown()
left(90)
forward(50)

# pintu
penup()
goto(-40, -97)
pendown()
right(90)
color("red")
begin_fill()
for i in range(2):
    forward(50)
    left(90)
    forward(80)
    left(90)
end_fill()

# pintu 
penup()
goto(-30, -60)
pendown()
color("black")
begin_fill()
circle(5)
end_fill()

hideturtle()
exitonclick()