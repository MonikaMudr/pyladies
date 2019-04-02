rodne_cislo = input('Zadej rodne cislo: ')

# a) je ve spravnem formatu, 6 cislic/4 cislice?
cislo_seznam = rodne_cislo.split('/')
if len(cislo_seznam[0]) == 6 and len(cislo_seznam[1]) == 4:
    print("Rodne cislo ma spravny format.")
cislo_bez_lomitka_string = ''.join(cislo_seznam)
cislo_bez_lomitka = int(cislo_bez_lomitka_string)

#b) je delitelne 11?
if cislo_bez_lomitka % 11 == 0:
    print('Zadane rodne cislo je delitelne 11')

#c) jake je datum narozeni (den, mesic, rok)
den = cislo_bez_lomitka_string[4:6]
mesic_string = cislo_bez_lomitka_string[2:4]
mesic = int(mesic_string)
if mesic > 50:
    mesic_zena_muz = mesic - 50
else:
    mesic_zena_muz = mesic
rok_string = cislo_bez_lomitka_string[0:2]
rok = int(rok_string)
if rok > 84:
    cely_rok = '{}{}'.format(19, rok)
else:
    cely_rok = '{}{}'.format(20, rok)
print("Datum narozeni je: " + '{}.{}.{}'.format(den, mesic_zena_muz, cely_rok))

#d) Pohlavi
if mesic > 50:
    print('Pohlavi: ' + 'zena')
else:
    print('Pohlavi:' + 'muz')
