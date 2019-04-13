from random import randrange

def vyhodnot(herni_pole):
    '''vyhodnoti herni pole piskvorek'''
    if "xxx" in herni_pole:
        return "x"
    elif "ooo" in herni_pole:
        return "o"
    elif '-' not in herni_pole:
        return "!"
    else:
        return "-"


def tah(herni_pole, cislo_pole, symbol):
    '''Vrati herni pole s danym symbolem umistenym na danou pozici'''
    return '{}{}{}'.format(herni_pole[:cislo_pole], symbol, herni_pole[(cislo_pole + 1):])



def tah_hrace(herni_pole, symbol):
    '''Zepta se na herni pole, vyhodnoti, zda je cislo 0-19 a zda je volna pozice, vrati nove herni pole'''
    while True:
        cislo_pole = int(input("Zadej cislo pozice, na kterou chces hrat: "))
        if 0 <= cislo_pole < len(herni_pole):
            if herni_pole[cislo_pole] == "-":
                return tah(herni_pole, cislo_pole, symbol)
            else:
                print("Toto pole je obsazene")
        else:
            print("Zadej cislo od 0 do 19")
            


def tah_pocitace(herni_pole, symbol):
    '''Vybere nahodne herni pozici 0-19 a na tu umisti symbol, vrati nove herni pole'''
    while True:
        cislo_pole = randrange(0, 20)
        if herni_pole[cislo_pole] == "-":
            return tah(herni_pole, cislo_pole, symbol)



#piskvorky1D:
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
