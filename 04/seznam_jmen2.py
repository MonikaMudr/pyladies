zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

spravne_zaznamy = []
chybne_zaznamy = []
opraveny_zaznam = []
for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    if jmeno.islower() or prijmeni.islower():
        chybne_zaznamy.append(zaznam)
    else:
        spravne_zaznamy.append(zaznam)

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    opraveny_zaznam.append('{} {}'.format(jmeno.capitalize(), prijmeni.capitalize()))


print(chybne_zaznamy) # → ['pepa novák', 'Ivo navrátil', 'jan Poledník']

print(spravne_zaznamy) # → ['Jiří Sládek']
print(opraveny_zaznam)