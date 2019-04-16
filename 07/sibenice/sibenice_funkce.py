from random import choice
def vyber_slova():
    '''pocitac vybira slovo ze seznamu, se kterym se bude hrat'''
    seznam_slov = ['pes', 'balon', 'mispule']
    return choice(seznam_slov)
def je_pismeno_ve_slove(pismeno, hadane_slovo):
    '''Zkontroluje, zda je zvolene pismeno v hadanem slove.'''
    if pismeno in hadane_slovo:
        return True
    else:
        return False

def vloz_pismeno(herni_pole, pismeno, hadane_slovo):
    '''Vlozi pismeno do slova na prislusnou pozici'''
    cislo_pozice = hadane_slovo.index(pismeno)
    return '{}{}{}'.format(herni_pole[:cislo_pozice], pismeno, herni_pole[(cislo_pozice + 1):])

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