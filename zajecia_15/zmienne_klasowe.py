from datetime import datetime
class Jablko:

    rodzaj = "owoc"

    def __init__(self, waga, cena_za_kg):
        #self.rodzaj = "owoc"
        self.waga = waga
        self.cena = self.oblicz_cene_jablka(cena_za_kg)

    def oblicz_cene_jablka(self, cena_za_kg):
        return self.waga * cena_za_kg

    def zmiana_rodzaju_jablka(self, nowy_rodzaj):
        self.rodzaj = nowy_rodzaj

    @classmethod
    def zmiana_rodzaju_jablka_dla_klasy(cls, nowy_rodzaj):
        cls.rodzaj = nowy_rodzaj

    @staticmethod
    def pobierz_timestamp_z_danej_operacji():
        return datetime.now()


jablko_golden = Jablko(waga=0.40, cena_za_kg=8.99)
jablko_papierowka = Jablko(waga=0.30, cena_za_kg=12.99)

#jablko_papierowka.rodzaj = "warzywo"
#jablko_golden.rodzaj = "warzywo"

Jablko.rodzaj = "klocek_lego"

jablko_papierowka.rodzaj = "warzywo"

jablko_3 = Jablko(waga=0.1, cena_za_kg=10.99)

#Jablko.rodzaj = "patyk"
#jablko_3.zmiana_rodzaju_jablka("granat") #to jest to samo co jablko_3.rodzaj = "granat"
jablko_3.zmiana_rodzaju_jablka_dla_klasy("shotgun") #to jest dokladnie to samo co Jablko.rodzaj = "shotgun"
print(jablko_3.rodzaj)
print(jablko_golden.rodzaj)
print(jablko_papierowka.rodzaj)
print(jablko_golden.pobierz_timestamp_z_danej_operacji())
