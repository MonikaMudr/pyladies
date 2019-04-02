from turtle import forward, left, exitonclick

n = int(input('Zadej n pro n-uhelnik: '))
vnitrni_uhel = 180 * (1 - 2/n)
vnejsi_uhel = 180 - vnitrni_uhel
puvodni_strana = 10
delka_strany = 10

for j in range(10):
    forward(delka_strany + j)
    left(vnejsi_uhel)
exitonclick()