import random
seznam = ['kámen', 'nůžky', 'papír']
def tah_pocitace2():
    return random.choice(['kámen', 'nůžky', 'papír'])
def tah_cloveka2():
    return input('kámen, nůžky, nebo papír? Pokud nechces pokracovat zadej konec. ')
while True:
    tah_cloveka = tah_cloveka2()
    tah_pocitace = tah_pocitace2()
    if tah_cloveka ==  tah_pocitace:
        print('Plichta.')
    elif tah_cloveka == 'nůžky' and tah_pocitace == 'papír' or tah_cloveka == 'kámen' and tah_pocitace == 'nůžky' or tah_cloveka == 'papír' and tah_pocitace == 'kámen':
        print('Vyhrála jsi!')
    elif tah_cloveka == 'papír'and tah_pocitace == 'nůžky' or tah_cloveka == 'nůžky' and tah_pocitace == 'kámen' or tah_cloveka == 'kámen' and tah_pocitace == 'papír':
        print('Počítač vyhrál.')
    elif tah_cloveka == "konec":
        break
    else:
        print('Nerozumím.')

