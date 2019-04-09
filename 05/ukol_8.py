import random

def hody_kostkou(hazene_cislo):
    '''Necha hazet hrace kostkou dokud nepadne urcite cislo(hazene_cislo), vrati seznam s jednotlivymi hody '''
    kostka = [1, 2, 3, 4, 5, 6]
    hod_kostkou = 0
    hody_hrace = []
    while hod_kostkou != hazene_cislo:
        hod_kostkou = random.choice(kostka)
        hody_hrace.append(hod_kostkou)
    return hody_hrace

def hody_vsech_hracu(pocet_hracu, hazene_cislo):
    '''Podle poctu hracu, vrati seznam obsahujici pro kazdeho hrace seznam s cislem hrace a s jeho hody '''
    seznam_hracu_a_hodu = []
    for poradi_hrace in range(pocet_hracu):
        seznam_hracu_a_hodu.append([poradi_hrace, hody_kostkou(hazene_cislo)])
    return seznam_hracu_a_hodu

seznam_hracu_a_hodu = hody_vsech_hracu(4, 6)
vyhravajici_hrac = seznam_hracu_a_hodu[0]
for hrac in seznam_hracu_a_hodu:
    if len(hrac[1]) > len(vyhravajici_hrac[1]):
        vyhravajici_hrac = hrac
    print('hody kostkou {}. hrace: {}'.format((hrac[0] + 1), hrac[1]))
print(("vyhral hrac c. {}".format(vyhravajici_hrac[0] + 1)))

