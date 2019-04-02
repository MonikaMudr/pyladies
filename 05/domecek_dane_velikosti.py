from turtle import forward, right, left, exitonclick
from math import sqrt




def domecek(delka_strany):
  "vykresli domecek dane velikosti"
  delka_sikme_strany = sqrt(2)*delka_strany
  delka_strecha = delka_sikme_strany/2
  left(90)
  forward(delka_strany)
  right(90)
  forward(delka_strany)
  right(135)
  forward(delka_sikme_strany)
  left(135)
  forward(delka_strany)
  left(90)
  forward(delka_strany)
  left(45)
  forward(delka_strecha)
  left(90)
  forward(delka_strecha)
  left(90)
  forward(delka_sikme_strany)
  left(45)
  forward(10)
  exitonclick()
domecek(200)