class Kocka:
    def _init_(self):
        self.pocet_zivotu = 9

    def zamnoukej(self):
        print('{}: Mnau!'.format(self.jmeno))

    def je_ziva(self):
        if pocet_zivotu != 0:
            print('{}: Jsem ziva!'.format(self.jmeno))
    def uber_zivot(self):
        pocet_zivotu -= 1
    def snez(self, jidlo):
        if 0 < pocet_zivotu < 9:
            if jidlo == 'ryba':
                pocet_zivotu += 1


class Kotatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def zamnoukej(self):
        print("{}: Mňau!".format(self.jmeno))

    def snez(self, jidlo):
        print("{}: Mňau mňau! {} mi chutná!".format(self.jmeno, jidlo))

mourek = Kotatko('Mourek')
mourek.zamnoukej()