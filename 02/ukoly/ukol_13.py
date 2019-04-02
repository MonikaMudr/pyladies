#program vypise, zde je tvuj pitny rezim dostatecny.
#idealni prijem tekutin se vypocita jako vaha (kg)*0.035
vypite_mnozstvi = int(input('Zadej mnozstvi tekutin, ktere vypijes za jeden den (v ml): '))
vaha = int(input('Zadej svou vahu (v kg): '))
idealni_prijem = vaha*0.035*1000
if vypite_mnozstvi >= 3999:
    print('trpis nejspis ziznivkou')
elif vypite_mnozstvi >= idealni_prijem + 250:
    print('par sklenic uber')
elif vypite_mnozstvi >= idealni_prijem - 250:
    print('tvuj denni prijem tekutin je idealni')
elif vypite_mnozstvi >= 250:
    print('Napij se vice')
else:
    print('Jsi snad Tarbikomys?')


