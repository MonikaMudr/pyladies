class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutna!".format(self.jmeno, jidlo))

class Kotatko(Zviratko):
    def zamnoukej(self):
        print('{}: Mnau!'.format(self.jmeno))

    def snez(self, jidlo):
        print('{} na {} chvili kouka!'.format(self.jmeno))
        super().snez(jidlo)

class Stenatko(Zviratko):
    def zastekej(self):
        print('{}: Haf!'.format(self.jmeno))


class Stenatko():
    def zastekej(self):
        print('Haf')
    def vydej_zvuk(self):
        self.zastekej()

class Hadatko(Zviratko):
    def __init__(self, jmeno):
        jmeno = jmeno.replace('s', 'sss')
        jmeno = jmeno.replace('S', 'Sss')
        super().__init__(jmeno)


standa = Hadatko('Stanislav')
standa.snez('myš')