def nacti_cislo():
    while True:
        otazka = input('Zadej cislo: ')
        try:
            return int(otazka)
        except ValueError:
            print('Nebylo to cislo')

print(nacti_cislo())