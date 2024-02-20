class Makowiec:

    def __init__(self, jajka_argument, drozdze_argument, mak_argument, maka_argument, mleko_argument):
        if jajka_argument > 10:
            self.jajka = 10
            print("Niestety nie mozesz miec wiecej niz 10 jajek")
        else:
            self.jajka = jajka_argument
        self.drozdze = drozdze_argument
        self.mak = mak_argument
        self.maka = maka_argument
        self.mleko = mleko_argument

    def rozbij_jajko(self):
        self.jajka -= 1

    def zrob_ciast(self):
        print("zrobiles ciasto")


makowiec_1 = Makowiec(jajka_argument=3, drozdze_argument=20, mak_argument=1000, mleko_argument=200, maka_argument=500)
makowiec_2 = Makowiec(jajka_argument=11, drozdze_argument=20, mak_argument=1000, mleko_argument=200, maka_argument=500)
print(makowiec_1.jajka)
print(makowiec_2.jajka)
makowiec_1.rozbij_jajko()
print(makowiec_1.jajka)
print(makowiec_2.jajka)
