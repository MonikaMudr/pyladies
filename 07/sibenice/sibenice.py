from obrazky import slovnik_sibenice
from sibenice_funkce import vyber_slova, vloz_pismeno, vyhodnot_prubeh_hry, kolikrat_ve_slove, nacti_pismeno

hrat_znovu = 'ano'

while hrat_znovu == 'ano':
    hadane_slovo = vyber_slova()
    herni_pole = '-' * len(hadane_slovo)
    print('hadane slovo:', herni_pole)
    neuspesne_pokusy = 0
    while True:
        if vyhodnot_prubeh_hry(herni_pole, neuspesne_pokusy) == 'prohra':
            print('Prohral jsi')
            break
        elif vyhodnot_prubeh_hry(herni_pole, neuspesne_pokusy) == 'vyhra':
            print('Gratuluji, vyhral jsi!')
            break
        elif vyhodnot_prubeh_hry(herni_pole, neuspesne_pokusy) == 'pokracuj':
            pismeno = nacti_pismeno()    
            if pismeno in hadane_slovo:
                kolikrat = kolikrat_ve_slove(pismeno, hadane_slovo)
                herni_pole = vloz_pismeno(herni_pole, pismeno, hadane_slovo, kolikrat)
                print('hadane_slovo: ', herni_pole)
                print(slovnik_sibenice[neuspesne_pokusy])
            else:
                neuspesne_pokusy += 1
                print('hadane_slovo: ', herni_pole)
                print(slovnik_sibenice[neuspesne_pokusy])
    hrat_znovu = input('Chces-li si zahrat znovu zadej ano: ')




