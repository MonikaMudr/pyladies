kosik = {'jablko': 'cervene', 'hruska': 'zelena', 'broskev': "oranzova", 'banan': 'zluty'}

shnily_kosik = {}

for ovoce, barva in kosik.items():
    shnily_kosik[ovoce] = 'hnedo-{}'.format(barva)
print(shnily_kosik)
    
    

    