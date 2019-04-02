from turtle import forward, left, exitonclick

n = 20
vnitrni_uhel = 180 * (1 - 2/n)
vnejsi_uhel = 180 - vnitrni_uhel
delka_strany = 1
left(90)

for j in range(500):
    forward(delka_strany)
    left(vnejsi_uhel)
    delka_strany = delka_strany + 0.1

exitonclick()