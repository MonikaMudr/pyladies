def spravny_format(rodne_cislo):
    try:
        int(rodne_cislo [:-5] + rodne_cislo [7:])
        if len(rodne_cislo) != 11 and rodne_cislo[6] != '/':
            raise ValueError
    except ValueError:
        print('Zadane cislo je ve spatnem formatu. Zkus to znovu!')
    else:
        return True

'''def nacti_RC():
    while True:
        rodne_cislo = input('Zadej rodne cislo ve formatu "xxxxxx/xxxx": ')
        try:
            int(rodne_cislo [:-5] + rodne_cislo [7:])
        except ValueError:
            print('Zadane rodne cislo neexistuje. Zkus to znovu!')
        else:
            return rodne_cislo'''

'''def spravny_format(rodne_cislo):
    cislo_bez_lomitka = rodne_cislo [:-5] + rodne_cislo [7:]
        if len(rodne_cislo.split('/')[0]) == 6 and len(rodne_cislo.split('/')[1]) == 4:
            return True
        else:
            return False'''

def delitelnost_11(rodne_cislo):
    "Zjisti, zda je rodne cislo delitelne 11"
    cislo_bez_lomitka = int(rodne_cislo [:-5] + rodne_cislo [7:])
    if cislo_bez_lomitka % 11 == 0:
        return True
    else:
        return False

def datum_narozeni(rodne_cislo):
    "Vraci datum narozeni"
    den = int(rodne_cislo[4:6])
    mesic = int(rodne_cislo[2:4])
    if mesic > 50:
        mesic -= 50
    rok = int(rodne_cislo[0:2])
    if rok > 84:
        cely_rok = '{}{}'.format(19, rok)
    else:
        cely_rok = '{}{}'.format(20, rok)
    return '{}.{}.{}'.format(den, mesic, cely_rok)

def existujici_datum_narozeni(rodne_cislo):
    "Vraci, zda den datumu narozeni je existujici datum"
    den = int(rodne_cislo[4:6])
    if den < 32:
        return True

def pohlavi(rodne_cislo):
    "Z rodneho cisla zjisti pohlavi"
    mesic = int(rodne_cislo[2:4])
    if mesic > 50:
        return "zena"
    else:
        return "muz"


while True:
    rodne_cislo = input('Zadej rodne cislo ve formatu "xxxxxx/xxxx": ')
    if spravny_format(rodne_cislo):
        if delitelnost_11(rodne_cislo) and existujici_datum_narozeni(rodne_cislo):
            print("Datum narozeni:", datum_narozeni(rodne_cislo))
            print("Pohlavi:", pohlavi(rodne_cislo))
            break
        else:   
            print("Zadane rodne cislo neexistuje")