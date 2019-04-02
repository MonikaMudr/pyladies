# tento program porovnava 2 seznamy, vypise jejich prunik, a seznam zvirat pouze v prvnim seznamu a pouze ve druhem seznamu

seznam1 = ['pes', 'kocka', 'kralik', 'had', 'andulka']
seznam2 = ['kachna', 'kocka', 'kun', 'prase', 'kralik']
seznam_prunik = []
pouze_seznam1 = []
pouze_seznam2 = []



for zvire in seznam1:
    if zvire in seznam2:
        seznam_prunik.append(zvire)
    else:
        pouze_seznam1.append(zvire)

for zvire2 in seznam2:
    if zvire2 not in seznam1:
        pouze_seznam2.append(zvire2)

print(seznam_prunik)
print(pouze_seznam1)
print(pouze_seznam2)
    
