#pokud zadam spravne heslo(kolotoc), program sdeli tajemstvi (rizek je v lednici).
heslo = input('Zadej heslo: ')
if heslo == 'kolotoc':
    heslo_spravne = True
    if heslo_spravne:
        print('Rizek je v lednici')
else:
    print('Spatne heslo')

