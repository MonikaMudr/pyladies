from turtle import forward, right, left, exitonclick, penup, pendown, getscreen, bgcolor, fillcolor, begin_fill, end_fill, pensize, color, setposition, setup, speed, home, pencolor
from random import sample

getscreen().bgcolor('#1E1E1D')
setup(800, 600)
speed(0)

############################# hvezdy ###################################
penup()
setposition(-400, 280)
pendown()
for posun in range(10): 
    y = 280 - (posun * 50)
    x = -400 + (posun * 7.5)
    setposition(x, y)
    pendown()
    for _ in range(8):
        fillcolor('#BDBD45')
        pencolor('#BDBD45')
        begin_fill()
        delka = [7, 10, 20, 25]
        strana_hvezda = sample(delka, 1)
        for i in range(5):
            forward(strana_hvezda[0])
            left(216)
        penup()
        forward(100)
        end_fill()

######################### mesic ####################################
penup()
setposition(-300, 280)
pendown()
pensize(10)
n = 100
vnitrni_uhel = 180 * (1 - 2/n)
vnejsi_uhel = 180 - vnitrni_uhel
delka_strany = 3
fillcolor('#DFDF1E')
pencolor('#D4D423')
begin_fill()
for _ in range(n):
    forward(delka_strany)
    right(vnejsi_uhel)
end_fill()

############################# hory_trojuhelniky ##################
penup()
setposition(-300, -220)
pendown()
pensize(1)
trojuhelnik_strana = 600
left(60)
fillcolor('#40404A')
pencolor('#40404A')
begin_fill()
for _ in range (3):
    forward(trojuhelnik_strana)
    right(120)
end_fill()

forward((trojuhelnik_strana / 5) * 4) # snehova spicka
fillcolor('#D6DFE2')
pencolor('#D6DFE2')
begin_fill()
for _ in range (3):
    forward(trojuhelnik_strana / 5)
    right(120)
end_fill()

penup() # presun pro druhou horu
right(180)
forward((trojuhelnik_strana / 5) * 4)
left(120)
forward(180)
pendown()
fillcolor('#79797F') # druha, mensi hora
pencolor('#79797F')
begin_fill()
for _ in range (3):
    forward(450)
    left(120)
end_fill()



###################### pulkruh ######################
home()
n = 100
vnitrni_uhel = 180 * (1 - 2/n)
vnejsi_uhel = 180 - vnitrni_uhel
delka_strany = 30
fillcolor('#21170D')
pencolor('#21170D')
begin_fill()
for _ in range(n):
    forward(delka_strany)
    right(vnejsi_uhel)
end_fill()

####################################  domecky ################################
setposition (0, 0)
sire_domu = 50
#zadni strana domu
penup()
setposition(-400, -220)
forward(sire_domu * 0.8)
pendown()
for _ in range(6): #6 domecku
    items = [80, 120, 160, 200]
    strana = sample(items, 1)
    okno = 15
    pensize(3)
    for _ in range (2): #vnejsi steny domu
        fillcolor("#40404A")
        pencolor("black")
        begin_fill()
        forward(sire_domu)
        left(90)
        forward(strana[0]) #nechapu proc to je definovane s nulou v hranate zavorce
        left(90)
        end_fill()

    forward(sire_domu / 2)
    left(90)
    for _ in range(2): # znamena, ze okno je 2x
        fillcolor('#1D1C46')
        penup()
        forward(strana[0] / 3)
        pendown()
        begin_fill()
        for _ in range(4): # okno
            forward(okno)
            right(90)
        end_fill()
    penup() #posunuti na strechu
    forward(strana[0] / 3)
    pendown()
    for _ in range(2): #komin
        fillcolor('black')
        begin_fill()
        forward(okno)
        left(90)
        forward(okno / 2)
        left(90)
        end_fill()
    penup() # vraceni se na spodni zakladnu doprostred domu
    left(180)
    forward(strana[0])
    left(90)
    pendown()

    penup() #posunuti pro nakresleni dalsiho domu
    forward(sire_domu*2)
    pendown()


#druha rada domu
penup()
setposition(-400, -260)
forward(sire_domu * 1.6)
pendown()
for _ in range(6): #6 domecku
    items = [80, 120, 160, 200]
    strana = sample(items, 1)
    okno = 15
    pensize(3)
    for _ in range (2): #vnejsi steny domu
        fillcolor('#515155')
        begin_fill()
        forward(sire_domu)
        left(90)
        forward(strana[0]) #nechapu proc to je definovane s nulou v hranate zavorce
        left(90)
        end_fill()

    forward(sire_domu / 2)
    left(90)
    for _ in range(2): # znamena, ze okno je 2x
        fillcolor('#1D1B55')
        penup()
        forward(strana[0] / 3)
        pendown()
        begin_fill()
        for _ in range(4): # okno
            forward(okno)
            right(90)
        end_fill()
    penup() #posunuti na strechu
    forward(strana[0] / 3)
    pendown()
    for _ in range(2): #komin
        fillcolor('black')
        begin_fill()
        forward(okno)
        left(90)
        forward(okno / 2)
        left(90)
        end_fill()
    penup() # vraceni se na spodni zakladnu doprostred domu
    left(180)
    forward(strana[0])
    left(90)
    pendown()

    penup() #posunuti pro nakresleni dalsiho domu
    forward(sire_domu*2)
    pendown()

# predni rada domu  
penup() # posunuti se na zacatek
setposition(-400, -300)
pendown()
for _ in range(7): #7 domecku
    items = [80, 120, 160, 200]
    strana = sample(items, 1)
    okno = 15
    pensize(3)
    for _ in range (2): #vnejsi steny domu
        fillcolor('#79797F')
        begin_fill()
        forward(sire_domu)
        left(90)
        forward(strana[0]) #nechapu proc to je definovane s nulou v hranate zavorce
        left(90)
        end_fill()

    forward(sire_domu / 2)
    left(90)
    for _ in range(2): # znamena, ze okno je 2x
        fillcolor('#1F1C7F')
        penup()
        forward(strana[0] / 3)
        pendown()
        begin_fill()
        for _ in range(4): # okno
            forward(okno)
            right(90)
        end_fill()
    penup() #posunuti na strechu
    forward(strana[0] / 3)
    pendown()
    for _ in range(2): #komin
        fillcolor('black')
        begin_fill()
        forward(okno)
        left(90)
        forward(okno / 2)
        left(90)
        end_fill()
    penup() # vraceni se na spodni zakladnu doprostred domu
    left(180)
    forward(strana[0])
    left(90)
    pendown()

    penup() #posunuti pro nakresleni dalsiho domu
    forward(sire_domu*2)
    pendown()

#################################################################




exitonclick()

