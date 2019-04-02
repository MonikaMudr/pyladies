# program se yepta na domaci zvire a vypie, zda je toto zvire v seznamu

domaci_zvirata = ['pes', 'kocka', 'kralik', 'had']
hledane_zvire = input("Zadej domaci zvire: ")

if hledane_zvire in domaci_zvirata:
    print('Zvire je v seznamu')
else:
    print('Zvire neni v seznamu')

   
