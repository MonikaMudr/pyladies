def tah_pocitace():
    return random.choice(['kámen', 'nůžky', 'papír'])
def tah_cloveka():
    return input('kámen, nůžky, nebo papír? Pokud nechces pokracovat zadej konec. ')

while tah_cloveka == 'konec':
    tah_pocitace()
    tah_cloveka()
    if tah_cloveka ==  tah_pocitace:
        print('Plichta.')
    elif tah_cloveka == 'nůžky' and tah_pocitace == 'papír' or tah_cloveka == 'kámen' and tah_pocitace == 'nůžky' or tah_cloveka == 'papír' and tah_pocitace == 'kámen':
        print('Vyhrála jsi!')
    elif tah_cloveka == 'papír'and tah_pocitace == 'nůžky' or tah_cloveka == 'nůžky' and tah_pocitace == 'kámen' or tah_cloveka == 'kámen' and tah_pocitace == 'papír':
        print('Počítač vyhrál.')
    else:
        print('Nerozumím.')