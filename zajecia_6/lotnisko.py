'''
Jesteś szefem firmy technologicznej tworzącej system zarządzania dla międzynarodowego lotniska. System ten ma obsługiwać dane związane z lotami, liniami lotniczymi, pasażerami oraz stewardessami. Każdy lot może mieć przypisanych wielu pasażerów i jedną stewardessę, natomiast linie lotnicze mogą obsługiwać nieograniczoną liczbę lotów. Celem jest stworzenie programu, który pozwoli na efektywne zarządzanie i dostarczanie właściwych informacji na potrzeby logistyki i obsługi klienta lotniska.

**Program do zarządzania danymi lotów na międzynarodowym lotnisku**
Program powinien umożliwić:
1. Dodanie nowych danych do systemu:
   - Pasażera z przypisanym numerem lotu.
   - Stewardessy z przypisanym numerem lotu.
   - Linii lotniczej, która może obsługiwać wiele różnych lotów.
2. Przeglądanie i zarządzanie istniejącymi informacjami:
   - Pobranie listy pasażerów danego lotu.
   - Znalezienie przypisanej linii lotniczej dla wybranego pasażera.
   - Wyświetlenie listy lotów danej linii lotniczej.
   - Otrzymanie listy wszystkich pasażerów dla lotu, którego stewardessą jest wybrana osoba.
**Polecenia programu**
Po uruchomieniu, program powinien wyświetlić menu z następującymi komendami:
- dodaj - przechodzi do menu dodawania nowych danych.
- przeglądaj - przechodzi do menu przeglądania i zarządzania danymi.
- zakończ - kończy działanie programu.
**Menu dodawania danych (dodaj):**
Użytkownik może wybrać:
- pasażer - dodanie pasażera wymaga wprowadzenia imienia i nazwiska, numeru lotu.
- stewardessa - dodanie stewardessy wymaga wprowadzenia imienia i nazwiska, numeru lotu, do którego jest przypisana.
- linia_lotnicza - dodanie linii lotniczej wymaga wprowadzenia jej nazwy.
- zakończ_dodawanie - powrót do głównego menu.
**Menu przeglądania i zarządzania danymi (przeglądaj):**
Użytkownik może wybrać:
- lot - wprowadzenie numeru lotu wyświetla listę pasażerów tego lotu.
- pasażer - wprowadzenie imienia i nazwiska pasażera wyświetla nazwę linii lotniczej.
- linia_lotnicza - wprowadzenie nazwy linii lotniczej wyświetla listę lotów obsługiwanych przez linię.
- stewardessa - wprowadzenie imienia i nazwiska stewardessy wyświetla listę pasażerów jej lotu.
- zakończ_przeglądanie - powrót do głównego menu.
**Zakończenie pracy programu**
Polecenie zakończ powoduje zamknięcie aplikacji.
'''
class Pasazer:
    def __init__(self, imie_z_inputu, nazwisko_z_inputu, numer_lotu_z_inputu, rok_urodzenia):
        self.imie = imie_z_inputu
        self.nazwisko = nazwisko_z_inputu
        self.numer_lotu = numer_lotu_z_inputu
        self.plec = "mezczyzna"
        self.wiek = self.oblicz_moj_wiek(rok_urodzenia)

    def oblicz_moj_wiek(self, wiek):
        return 2024-wiek

    def __repr__(self):
        return f"Pasażer {self.imie} {self.nazwisko} z lotu {self.numer_lotu}"


class LiniaLotnicza:
    def __init__(self, lista_lotow, nazwa):
        self.nazwa = nazwa
        self.lista_lotow = lista_lotow

    def __repr__(self):
        return f"Linia lotnicza {self.nazwa} z lotami {self.lista_lotow}"


class Stewardessa:
    def __init__(self, imie, nazwisko, numer_lotu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_lotu = numer_lotu

    def __repr__(self):
        return f"Stewardessa {self.imie} {self.nazwisko} z lotu {self.numer_lotu}"

lotnisko = {
    "pasazerowie": [],
    "linie_lotnicze": [],
    "stewardessy": []
}


pasazerowie = [Pasazer(imie_z_inputu="Michal", nazwisko_z_inputu="Zietkowski", numer_lotu_z_inputu="LOT123", rok_urodzenia=1995),
               Pasazer(imie_z_inputu="Adam", nazwisko_z_inputu="Nowak", numer_lotu_z_inputu="LOT121", rok_urodzenia=1993),
               Pasazer(imie_z_inputu="Adam", nazwisko_z_inputu="Kowalski", numer_lotu_z_inputu="LOT125", rok_urodzenia=1993)]
linie_lotnicze = [LiniaLotnicza(nazwa="Lot", lista_lotow=["LOT123", "LOT121", "LOT125"]),
                  LiniaLotnicza(nazwa="Ryanair", lista_lotow=["RY123"])]
stewardessy = [Stewardessa(imie="Ania", nazwisko="Nowak", numer_lotu="LOT123"),
               Stewardessa(imie="Jacek", nazwisko="Bialoglowy", numer_lotu="RY123")]


def znajdz_pasazerow_lotu(numer_lotu):
    lista_pasazerow_lotu = []
    for pasazer in pasazerowie:
        if pasazer.numer_lotu == numer_lotu:
            lista_pasazerow_lotu.append(pasazer)
    return lista_pasazerow_lotu

def znajdz_numer_lotu_pasazera(imie, nazwisko):
    for pasazer in pasazerowie:
        if pasazer.imie == imie and pasazer.nazwisko == nazwisko:
            return pasazer.numer_lotu

def znajdz_linie_lotow_obslugujacych_trase(numer_lotu):
    for linia_lotnicza in linie_lotnicze:
        if numer_lotu in linia_lotnicza.lista_lotow:
            return linia_lotnicza.nazwa

def znajdz_linie_lotow_stewardessy(imie_stewardessy, nazwisko_stewardessy):
    for stewardessa in stewardessy:
        if stewardessa.imie == imie_stewardessy and stewardessa.nazwisko == nazwisko_stewardessy:
            return stewardessa.numer_lotu

koniec_programu = False
while not koniec_programu:
    #while koniec_programu==False
    print(pasazerowie)
    print(linie_lotnicze)
    print(stewardessy)
    print("Witaj w programie obsługi lotniska. Wybierz komendę, którą chcesz wykonać")
    operacja = input("1. Dodaj\n2. Zarządzaj\n3. Koniec programu\n")
    if operacja == "1":
        opcja_do_dodania = input("Co chcesz dodać?\n1. Pasażer\n2. Linia lotnicza\n3. Stewardessa\n")
        if opcja_do_dodania == "1":
            imie_pasazera = input("Podaj imię pasażera: ")
            nazwisko_pasażera = input("Podaj nazwisko pasażera: ")
            numer_lotu = input("Podaj numer lotu: ")
            rok_urodzenia = int(input("Podaj rok urodzenia: "))
            pasazerowie.append(Pasazer(imie_z_inputu=imie_pasazera, nazwisko_z_inputu=nazwisko_pasażera,
                                       numer_lotu_z_inputu=numer_lotu, rok_urodzenia=rok_urodzenia))
        elif opcja_do_dodania == "2":
            # lista_lotow = input("Podaj listę lotów: ")
            # lista_lotow.split(",")
            lista_lotow = []
            lot_do_dodania = True
            while lot_do_dodania:
                nowy_lot = input("Dodaj nowy lot: ")
                if nowy_lot != "":
                    lista_lotow.append(nowy_lot)
                else:
                    lot_do_dodania = False
            pass
    elif operacja == "2":
        opcja_do_zarzadzania = input("Czym chcesz zarządzać?\n1. Lot\n2. Pasażer\n3. Linia lotnicza\n4. Stewardessa")
        if opcja_do_zarzadzania == "1":
            numer_lotu_z_inputu = input("Podaj numer lotu: ")
            pasazerowie_lotu = znajdz_pasazerow_lotu(numer_lotu=numer_lotu_z_inputu)
            print(pasazerowie_lotu)
        elif opcja_do_zarzadzania == "2":
            imie_pasazera = input("Podaj imię pasażera: ")
            nazwisko_pasażera = input("Podaj nazwisko pasażera: ")
            numer_lotu_pasazera = znajdz_numer_lotu_pasazera(imie_pasazera, nazwisko_pasażera)
            nazwa_linii_lotniczej = znajdz_linie_lotow_obslugujacych_trase(numer_lotu_pasazera)
            print(f"Linia {nazwa_linii_lotniczej} obsługuje lot tego pasażera")
        elif opcja_do_zarzadzania == "4":
            imie_stewardessy = input("Podaj imię stewardessy: ")
            nazwisko_stewardessy = input("Podaj nazwisko stewardessy: ")
            numer_lotu_stewardesy = znajdz_linie_lotow_stewardessy(imie_stewardessy, nazwisko_stewardessy)
            pasazerowie_lotu = znajdz_pasazerow_lotu(numer_lotu_stewardesy)
            print(pasazerowie_lotu)
    elif operacja == "3":
        koniec_programu = True
    else:
        print("Nie mamy takiej komendy")