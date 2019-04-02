zaznamy = ['pepa novak', 'Jiri Sladek', 'Ivo navratil', 'jan Polednik']
spravne_zaznamy = []
spatne_zaznamy = []



for i in zaznamy:
    jmeno, prijmeni = i.split()
    if not jmeno[0].islower() and not prijmeni[0].islower():
        spravne_zaznamy.append(i)
    else:
        spatne_zaznamy.append(i)

print(spravne_zaznamy)
print(spatne_zaznamy)
