def nacti_cislo():
    while True:
        otazka = input('Zadej cislo: ')
        try:
            cislo = int(otazka)
        except ValueError:
            print('Nebylo to cislo')
        else:
            return cislo

print(nacti_cislo())