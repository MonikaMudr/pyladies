romal = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
arabic = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

slovnik_cislice = dict(zip((romal), (arabic)))
rimska_cislice = input("Zadej rimskou cislici: ")
pozice = 0
vysledek = 0

for symbol, hodnota in slovnik_cislice.items():
    pocet_symbolu = 0
    while rimska_cislice[pozice:(pozice + len(symbol))] == symbol:
        pocet_symbolu = pocet_symbolu + 1
        pozice += len(symbol)
    vysledek += pocet_symbolu * hodnota
print(slovnik_cislice)
print(vysledek)