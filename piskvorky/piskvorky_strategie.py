from pole import tah, vyhodnot, tah_hrace
from ai import tah_pocitace, tah_pocitace_strategie_vlevo, tah_pocitace_strategie_vpravo
            

def piskvorky1D():
    herni_pole = "-" * 20
    print('herni pole: ', herni_pole)
    cislo_kola = 1
    while True:
        herni_pole = tah_hrace(herni_pole, 'x')
        kolo_pole = '{}.kolo: {}'.format(cislo_kola, herni_pole)
        if vyhodnot(herni_pole) == "x":
            print(kolo_pole)
            print("Vyhral jsi")
            break
        elif vyhodnot(herni_pole) == "!":
            print(kolo_pole)
            print('Remiza')
            break
        herni_pole = tah_pocitace(herni_pole, "o")
        kolo_pole = '{}.kolo: {}'.format(cislo_kola, herni_pole)
        if vyhodnot(herni_pole) == "o":
            print(kolo_pole)
            print("Vyhral pocitac")
            break
        elif vyhodnot(herni_pole) == "!":
            print(kolo_pole)
            print('Remiza')
            break
        print(kolo_pole)
        cislo_kola += 1

