class Produkt:

    nazwa_sklepu = "Media Markt"

    def __init__(self, nazwa, cena, ilosc_sztuk):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc_sztuk = ilosc_sztuk

    def zmien_nazwe(self, nowa_nazwa):
        self.nazwa = nowa_nazwa

    def zmien_cene(self, cena):
        self.cena = cena

    def sprzedaj_produkt(self):
        self.ilosc_sztuk -= 1

    def __repr__(self):
        return f"{self.nazwa}"

    # def sprawdz_klase_energetyczna_produktu(self):
    #     if self.rodzaj_produktu == "TV":
    #         return "B"
    #     elif self.rodzaj_produktu == "Telefon":
    #         return "AA"
    #     elif self.rodzaj_produktu == "Peryferie":
    #         return "C"
    #     else:
    #         return "G"

class ProduktRTV(Produkt):

    rodzaj_produktu = "RTV"

    def __init__(self, nazwa, cena, ilosc_sztuk):
        super().__init__(nazwa, cena, ilosc_sztuk)
        self.gwarancja = True
        self.dlugosc_gwarancji = 365

    def zmniejsz_dzien_gwarancji(self):
        self.dlugosc_gwarancji -= 1

    def sprawdz_mnie(self):
        print("Produkt RTV")

class GwarancjaPlus:
    gwarancja_plus = True

    def skorzystaj_z_gwarancji(self):
        print("Skorzystalem z gwarancji plus!")

    def sprawdz_mnie(self):
        print("Gwarancja Plus")

class ProduktSpozywczy(Produkt):

    rodzaj_produktu = "spozywczy"


class ProduktRTV_Z_GwarancjaPlus(ProduktRTV, GwarancjaPlus):

    def sprzedaj_produkt(self):
        self.ilosc_sztuk -= 2

    def sprawdz_mnie(self):
        super().sprawdz_mnie()
        print("ProduktRTVZGwarancjaPLus")




telewizor_50_cali = ProduktRTV(nazwa="LG 50 cali TV UHD", cena=4999, ilosc_sztuk=40)
iphone_15 = ProduktRTV(nazwa="IPhone 15", cena=4500, ilosc_sztuk=100)
kabel_hdmi = ProduktRTV(nazwa="Kabel HDMI", cena=89, ilosc_sztuk=500)
woda_cisowianka = ProduktSpozywczy(nazwa="Woda cisowianka 0.5l", cena=1.5, ilosc_sztuk=1000)
guma_balonowa = Produkt(nazwa="hubba bubba", cena=2.0, ilosc_sztuk=50)
print(telewizor_50_cali)
print(woda_cisowianka.nazwa)
print(woda_cisowianka.ilosc_sztuk)
woda_cisowianka.sprzedaj_produkt()
print(woda_cisowianka.ilosc_sztuk)
print(woda_cisowianka.nazwa_sklepu)
print(guma_balonowa)
telewizor_65_cali_z_extra_gwarancja = ProduktRTV_Z_GwarancjaPlus(nazwa="Samsung 65 cali 4K", cena=8999, ilosc_sztuk=10)
telewizor_65_cali_z_extra_gwarancja.skorzystaj_z_gwarancji()
telewizor_65_cali_z_extra_gwarancja.sprzedaj_produkt()
print(telewizor_65_cali_z_extra_gwarancja.ilosc_sztuk)
telewizor_65_cali_z_extra_gwarancja.sprawdz_mnie()