from random import choice
def vyber_slova():
    '''pocitac vybira slovo ze seznamu, se kterym se bude hrat'''
    seznam_slov = ['kolobezka', 'oko', 'emental']
    return choice(seznam_slov)

def nacti_pismeno():
    '''Nacita pismeno od uzivatele tak dlouho, dokud nezada pismeno'''
    abeceda = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        pismeno = input('Zadej pismeno: ')
        if len(pismeno) == 1 and pismeno in abeceda:
            return pismeno
        else:
            print ('To nebylo pismeno. Zkus to znovu!')
            
def kolikrat_ve_slove(pismeno, hadane_slovo):
    '''Zjisti kolikrat je pismeno ve slove'''
    kolikrat = 0
    for i in hadane_slovo:
        if i == pismeno:
            kolikrat += 1
    return kolikrat

def vloz_pismeno(herni_pole, pismeno, hadane_slovo, kolikrat):
    '''Vlozi pismeno do slova na prislusnou pozici'''
    zacatek = 0
    for i in range(kolikrat):
        cislo_pozice = hadane_slovo.index(pismeno, zacatek)
        herni_pole = '{}{}{}'.format(herni_pole[:cislo_pozice], pismeno, herni_pole[(cislo_pozice + 1):])
        zacatek = cislo_pozice + 1
    return herni_pole

def vyhodnot_prubeh_hry(herni_pole, neuspesne_pokusy):
    '''Vezme herni pole a vyhodnoti, zda hrac jeste neprohral (neuspesne_pokusy jsou 10), ci nevyhral (ve slove
    neni volna pozice)'''
    if neuspesne_pokusy < 10:
        if '-' in herni_pole:
            return 'pokracuj'
        else:
            return 'vyhra'
    else:
        return 'prohra'