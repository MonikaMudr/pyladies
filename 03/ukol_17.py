prvni = int(input('Zadej prvni cislo: '))
druhe = int(input('Zadej prvni cislo: '))
treti = int(input('Zadej prvni cislo: '))
ctvrte = int(input('Zadej prvni cislo: '))
pate = int(input('Zadej prvni cislo: '))

muj_seznam = [prvni, druhe, treti, ctvrte, pate]
minimum = muj_seznam[0]
for cislo in muj_seznam:
    if cislo < minimum:
        minimum = cislo

print("Nejmensi zadane cislo je: ", minimum)
    