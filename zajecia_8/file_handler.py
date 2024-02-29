import json


class FileHandler:
    def __init__(self, sciezka_do_pliku_z_historia, sciezka_do_pliku_z_ksiegozbiorem_i_saldem):
        self.plik_z_historia: str = sciezka_do_pliku_z_historia
        self.plik_z_ksiegozbiorem_i_saldem: str = sciezka_do_pliku_z_ksiegozbiorem_i_saldem

    def odczyt_danych_z_pliku_z_ksiegozbiorem_i_saldem(self):
        with open(self.plik_z_ksiegozbiorem_i_saldem) as plik:
            dane = json.loads(plik.read())
            dane.get("budzet")
            print((dane.get("budzet"), dane.get("ksiegozbior")))
            return (dane.get("budzet"), dane.get("ksiegozbior"))

    def odczyt_danych_z_pliku_z_historia(self):
        with open(self.plik_z_historia) as plik:
            dane = json.loads(plik.read())
            return dane

    def zapis_do_pliku_z_ksiegozbiorem_i_saldem(self, budzet, ksiegozbior):
        with open(self.plik_z_ksiegozbiorem_i_saldem, mode="w") as file:
            file.write(json.dumps({
                "budzet": budzet,
                "ksiegozbior": ksiegozbior
            }))
