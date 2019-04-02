rodne_cislo = input('Zadej rodne cislo: ')

# a) je ve spravnem formatu, 6 cislic/4 cislice?
cislo_seznam = rodne_cislo.split('/')
if len(cislo_seznam[0]) == 6 and len(cislo_seznam[1]) == 4:
    cislo_format = True
else:
    cislo_format = False
cislo_bez_lomitka_string = ''.join(cislo_seznam)
cislo_bez_lomitka = int(cislo_bez_lomitka_string)

# je delitelne 11?
if cislo_bez_lomitka % 11 == 0:
    delitelne = True
else:
    delitelne = False

if cislo_format and delitelne:
    print("Zadane rodne cislo je realne")
else:
    print('Neexistujici rodne cislo')
