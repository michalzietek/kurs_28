class Zwierze:
    def __init__(self, nazwa, typ):
        self.nazwa = nazwa
        self.typ = typ

    def podaj_mi_swoja_nazwe(self):
        print(self.nazwa)


class Lew(Zwierze):

    def zarycz(self):
        print("Rawrrrr")



class Glonojad(Zwierze):

    def plywaj(self):
        print("Plywam")


class MalyLew(Lew):
    def jestem_maly(self):
        print("jestem maly")

lew = Lew(nazwa="lew", typ="ssak")
maly_lew = MalyLew(nazwa="maly lew", typ="ssak")
glonojad = Glonojad(nazwa="glonojad", typ="ryba")
lew.podaj_mi_swoja_nazwe()
glonojad.podaj_mi_swoja_nazwe()
lew.zarycz()
glonojad.plywaj()
maly_lew.podaj_mi_swoja_nazwe()