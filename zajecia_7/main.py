from greeting import witaj_uzytkowniku, zegnaj_uzytkowniku
from zajecia_6.klasy.pasazer import Pasazer
from helpers import oblicz_dane_figury

# imie_uzytkownika = input("Cześć! Podaj mi swoje imię: ")
# witaj_uzytkowniku(imie_uzytkownika)
# zegnaj_uzytkowniku(imie_uzytkownika)
# pasazer = Pasazer(imie_z_inputu=imie_uzytkownika, nazwisko_z_inputu="Zietkowski", numer_lotu_z_inputu="LOT123", rok_urodzenia=1999)
# print(pasazer)

figura = input("Podaj rodzaj figury: ")
oblicz_dane_figury(figura)
