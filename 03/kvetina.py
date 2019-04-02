from turtle import forward, left, exitonclick, shape, right, speed, penup, pendown
speed(8)

for i in range(18):
    for opakovani in range(4):
        forward(50)
        left(90)
    left(20)
right(90)
forward(80)

for j in range(6):
    left(50)

    for _ in range(20):
        forward(5)
        left(4)
    left(100)
    for _ in range(20):
        forward(5)
        left(4)
    left(50)

    forward(20)
    right(50)

    for _ in range(20):
        forward(5)
        right(4)
    right(100)
    for _ in range(20):
        forward(5)
        right(4)
    right(50)
    forward(20)


exitonclick()