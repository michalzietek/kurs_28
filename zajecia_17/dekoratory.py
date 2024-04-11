# imie = "Michał"
# print(type(imie))
#
# def przywitaj_sie():
#     print(f"Hello {imie}")
#     return "aaaa"
#
#
#
# przywitaj_sie()
#
# wartosc_z_funkcji = przywitaj_sie()
#
# print(wartosc_z_funkcji)
# print(type(wartosc_z_funkcji))
#
# zmienna_funkcja = przywitaj_sie
# zmienna_funkcja() # przywitaj_sie()
# print(type(zmienna_funkcja))
# print(zmienna_funkcja)
#
# def wyswietl_imie():
#     print(f"Twoje imię to {imie}")
#     #return przywitaj_sie()
#     return przywitaj_sie
#
#
# przywitaj_sie_zmienna = wyswietl_imie()
# print(type(przywitaj_sie_zmienna))
# przywitaj_sie_zmienna()
# wyswietl_imie_zmienna = wyswietl_imie
#
#
# def wyswietl_mi_tekst(funkcja):
#     print("Instrukcje do wykonania przed funkcja")
#     funkcja()
#     print("Instrukcja po wykonaniu funkcji")
#
# def oblicz_mi_dodawanie():
#     print(f"Wynik dodawania 2 + 2: {2 + 2}")
#
# wynik_dodawania = oblicz_mi_dodawanie
#
# wyswietl_mi_tekst_zmienna = wyswietl_mi_tekst # dojdziemy do rekurencji - nigdy się nie skończy
# wyswietl_mi_tekst(wynik_dodawania)
# wyswietl_mi_tekst(wyswietl_imie_zmienna)
# wyswietl_mi_tekst(przywitaj_sie_zmienna)


#############################################################################################

def moj_dekorator(funkcja):
    def opakowacz():
        print("Instrukcje przed wywołaniem funkcji")
        funkcja()
        print("Instrukcje po wywołaniu funkcji")
    return opakowacz

@moj_dekorator
def przywitanie():
    print("Witaj świecie!")


# przywitanie()
#
# przywitanie()
#
# def sprawdz_zalogowanie(funkcja):
#     def wrapper(*args, **kwargs):
#         print("Sprawdzam czy użytkownik jest zalogowany")
#         funkcja(*args, **kwargs)
#     return wrapper
#
# @sprawdz_zalogowanie
# def dodaj_do_znajomych(nowy_uzytkownik):
#     print(f"Dodano do znajomych {nowy_uzytkownik}")
#
# dodaj_do_znajomych("Adam Małysz")



def zapytaj_o_potwierdzenie_2fa(funkcja):
    def wrapper(*args, **kwargs):
        print("Na twój telefon został wysłany kod pin")
        kod_pin = input("Podaj kod: ")
        if kod_pin == "0000":
            funkcja(*args, **kwargs)
            print("Operacja została wykonana.")
        else:
            print("Niestety kod pin nie jest poprawny")
    return wrapper


@zapytaj_o_potwierdzenie_2fa
def wyslij_przelew_bankowy(kwota):
    print(f"Wysłano przelew bankowy na kwotę {kwota}")

wyslij_przelew_bankowy(1000)