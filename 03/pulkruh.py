from turtle import forward, left, exitonclick, penup, pendown

n = 100
vnitrni_uhel = 180 * (1 - 2/n)
vnejsi_uhel = 180 - vnitrni_uhel
delka_strany = 200/n

penup()
for _ in range(int(n/4)):
    forward(delka_strany)
    left(vnejsi_uhel)
pendown()
for _ in range(int(n/2)):
    forward(delka_strany)
    left(vnejsi_uhel)

exitonclick()