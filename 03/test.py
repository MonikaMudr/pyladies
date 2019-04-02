from turtle import forward, left, exitonclick, penup, pendown, setposition, fillcolor, begin_fill, end_fill

n = 100
vnitrni_uhel = 180 * (1 - 2/n)
vnejsi_uhel = 180 - vnitrni_uhel
delka_strany = 12
penup()
setposition(0, -400)
fillcolor('black')
begin_fill()
for _ in range(int(n/4)):
    forward(delka_strany)
    left(vnejsi_uhel)
pendown()
for _ in range(int(n/2)):
    forward(delka_strany)
    left(vnejsi_uhel)
end_fill()

exitonclick()