
strana = float(input('Zadej stranu čtverce v centimetrech: '))
pravda = strana > 0
if pravda:
    print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
    print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')
else:
    print('zadana hodnota musi byt kladne cislo')