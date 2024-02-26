class Pasazer:
    def __init__(self, imie_z_inputu, nazwisko_z_inputu, numer_lotu_z_inputu, rok_urodzenia):
        self.imie = imie_z_inputu
        self.nazwisko = nazwisko_z_inputu
        self.numer_lotu = numer_lotu_z_inputu
        self.plec = "mezczyzna"
        self.wiek = self.oblicz_moj_wiek(rok_urodzenia)

    def oblicz_moj_wiek(self, wiek):
        return 2024-wiek