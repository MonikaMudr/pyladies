strana = float(input('Zadej cislo'))
cislo_je_spravne = strana > 0
if cislo_je_spravne:
    print('Obvod ctverce se stranou', strana, 'cm je', 4 * strana, 'cm')
    print('Obsah stverce se stranou', strana, 'cm je', strana * strana, 'cm2')
else:
    print('Zadej kladne cislo')
