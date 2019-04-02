from turtle import forward, left, exitonclick, right

n = 100
vnitrni_uhel = 180 * (1 - 2/n)
vnejsi_uhel = 180 - vnitrni_uhel
delka_strany = 200 / n

for _ in range(n):
    forward(delka_strany)
    right(vnejsi_uhel)

exitonclick()