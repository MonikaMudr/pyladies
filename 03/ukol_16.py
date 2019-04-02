prvni_cislo = int(input('Zadej prvni cislo: '))
druhe_cislo = int(input('Zadej druhe cislo: '))
operace = input('Zadej pocetni operaci (+, -, *, /): ')
if operace == '+':
    vysledek = prvni_cislo + druhe_cislo
elif operace == '-':
    vysledek = prvni_cislo - druhe_cislo
elif operace == '*':
     vysledek = prvni_cislo * druhe_cislo
else:
     vysledek = prvni_cislo / druhe_cislo
print(str(prvni_cislo) + ' ' + operace + ' ' + str(druhe_cislo), '=', vysledek)