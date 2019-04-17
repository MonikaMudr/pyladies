def tah(herni_pole, cislo_pole, symbol):
    '''Vrati herni pole s danym symbolem umistenym na danou pozici'''
    return '{}{}{}'.format(herni_pole[:cislo_pole], symbol, herni_pole[(cislo_pole + 1):])

def vyhodnot(herni_pole):
    '''vyhodnoti herni pole piskvorek'''
    if "xxx" in herni_pole:
        return "x"
    elif "ooo" in herni_pole:
        return "o"
    elif '-' not in herni_pole:
        return "!"
    else:
        return "-"

def tah_hrace(herni_pole, symbol):
    '''Zepta se na herni pole, vyhodnoti, zda je cislo 0-19 a zda je volna pozice, vrati nove herni pole'''
    while True:
        cislo_pole = int(input("Zadej cislo pozice, na kterou chces hrat: "))
        if 0 <= cislo_pole < len(herni_pole):
            if herni_pole[cislo_pole] == "-":
                return tah(herni_pole, cislo_pole, symbol)
            else:
                print("Toto pole je obsazene")
        else:
            print("Zadej cislo od 0 do 19")