from math import pi
def obvod_elipsy(a, b):
    return pi * a * b

def obsah_eliptickeho_valce(a, b, vyska):
    obvod = obvod_elipsy(a, b)
    return obvod * vyska

print(obsah_eliptickeho_valce(2, 4, 4))