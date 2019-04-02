def spravny_format(rodne_cislo):
    "Kontroluje spravny format rodneho cisla: 6 cisel + '/' + 4 cisla"
    cislo_bez_lomitka = rodne_cislo [:-5] + rodne_cislo [7:]
    if cislo_bez_lomitka.isdecimal():
        if len(rodne_cislo.split('/')[0]) == 6 and len(rodne_cislo.split('/')[1]) == 4:
            return True
        else:
            return False
    else:
        return False
print(spravny_format("85kl17/4655"))
