from piskvorky import tah
from random import randrange
def tah_pocitace_bez_strategie(herni_pole, symbol):
    '''Vybere nahodne herni pozici 0-19 a na tu umisti symbol, vrati nove herni pole'''
    while True:
        cislo_pole = randrange(0, 20)
        if herni_pole[cislo_pole] == "-":
            return tah(herni_pole, cislo_pole, symbol)

def tah_pocitace_strategie_vlevo(herni_pole, symbol, podretezec):
    '''tah pocitace v pripade, ze se volna pozice nachazi nalevo od hracich symbolu (napr. -oo).'''
    cislo_pole = herni_pole.index(podretezec)
    return tah(herni_pole, cislo_pole, symbol)

def tah_pocitace_strategie_vpravo(herni_pole, symbol, podretezec):
    '''tah pocitace v pripade, ze se volna pozice nachazi napravo od hracich symbolu (napr. oo-).'''
    cislo_pole = herni_pole.index(podretezec) + len(podretezec) - 1
    return tah(herni_pole, cislo_pole, symbol)

def tah_pocitace(herni_pole, symbol):
    if "-oo" in herni_pole:
        return tah_pocitace_strategie_vlevo(herni_pole, 'o', "-oo")
    elif "oo-" in herni_pole:
        return tah_pocitace_strategie_vpravo(herni_pole, "o", "oo-")
    elif "-xx" in herni_pole:
        return tah_pocitace_strategie_vlevo(herni_pole, 'o', "-xx")
    elif "-o-" in herni_pole:
        return tah_pocitace_strategie_vlevo(herni_pole, 'o', "-o-")
    elif "xx-" in herni_pole:
        return tah_pocitace_strategie_vpravo(herni_pole, "o", "xx-")
    elif "-o" in herni_pole:
        return tah_pocitace_strategie_vlevo(herni_pole, 'o', "-o")
    elif "-x" in herni_pole:
        return tah_pocitace_strategie_vlevo(herni_pole, "o", "-x")
    else:
        return tah_pocitace_bez_strategie(herni_pole, 'o')
    