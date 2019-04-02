from random import randrange
score = 0

while score < 21:
    print('Score:', score)
    pokracovani = input('Chces pokracovat (ano/ne)?')
    if pokracovani == 'ne':
        break
    elif pokracovani == 'ano':
        karta = randrange(2, 11)
        print("Hodnota karty je", karta)
        score = score + karta
    else:
        print('Odpovez ano ci ne')
if score <= 21:
    print('Tve konecne score je ', score)
else:
    print('Prohrals')