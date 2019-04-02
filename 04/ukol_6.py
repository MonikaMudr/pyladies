# tento program radi zvirata v seznamu podle abecedy, ale ignoruje prvni pismeno.

domaci_zvirata = ['pes', 'kocka', 'kralik', 'had', 'andulka']
seznam_v_seznamu = []
seznam_2 = []
for zvire in domaci_zvirata:
    seznam_v_seznamu.append([zvire[1:], zvire])
seznam_v_seznamu.sort()
for klic, zvire_2 in seznam_v_seznamu:
    seznam_2.append(zvire_2)

print(seznam_2)


