# ############# LISTY ######################
# produkty = ["jajka", "mleko", "mąka"]
# print(produkty)
# print(type(produkty))
# #pobieranie danych z listy
# print(produkty[0])
# #dodawanie danych do listy
# produkty.append("jabłka")
# pozycja_jablka = 10
# produkty.insert(pozycja_jablka, "woda")
# print(produkty)
# #produkty[pozycja_jablka] uwazac na indexy w listach
# #zmiana danych w liscie
# produkty[0] = "energeryk"
# print(produkty)
# #operacja usuwania z listy
# del(produkty[0])
# produkty.remove("mleko")
# print(produkty)
# for produkt in produkty:
#     print(produkt)
#     produkt = "harmonia"
#
# for moja_wlasna_zmienna, produkt in enumerate(produkty):
#     print(moja_wlasna_zmienna, produkt)
#     if moja_wlasna_zmienna == 0:
#         produkty[moja_wlasna_zmienna] = "harmonia"
#
# print(produkty)
# # print("Proszę podaj mi listę swoich zakupów")
# # lista_zakupow = ""
# # koniec_programu = False
# # while not koniec_programu:
# #     nowy_produkt = input("Proszę dodaj mi produkt do listy: ")
# #     if nowy_produkt == "":
# #         koniec_programu = True
# #     else:
# #         print(f"Dodałeś nowy produkt {nowy_produkt}")
# #         lista_zakupow += f"{nowy_produkt}, "
# # print(nowy_produkt)
# # print(lista_zakupow)
# lista_waznych_zmiennych = ["jablko", 12, True, 33.99, "jablko"]
#
#
# ########### KROTKI ################
# krotka_produktow = ("Jajka", "Mąka", "Mleko", "Szampon")
# plci = ("Mezczyzna", "Kobieta", "Nie chce podawac", "Mezczyzna")
# pusta_krotka = ()
# #krotka_produktow[0] = "Książka" nie ma mozliwosci dodawania ani zmiany wartosci
# #print(plci[0])
# for plec in plci:
#     print(plec)
#
# ############ ZBIORY ###############
# zbior_liczb = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3}
# zbior_liczb.add(10)
# zbior_liczb.remove(7)
# print(zbior_liczb)
# #print(zbior_liczb[0])
# print(11 in zbior_liczb)
# for liczba in zbior_liczb:
#     print(liczba)
#
# #for do usuwania wartosci 10 i zamiany na 8
# for liczba in zbior_liczb:
#     if liczba == 10:
#         zbior_liczb.remove(liczba)
#         zbior_liczb.add(8)
#
# ciekawy_zbior = {True}
# print(1 == True)
# print(ciekawy_zbior)

####### SŁOWNIKI #########
uzytkownik_systemu = ["michal123", "michalzietkowski@gmail.com", "haslo123", "mezczyzna", "Michal", "Zietkowski"]
imie = uzytkownik_systemu[4]
nazwisko = uzytkownik_systemu[5]
imie = "Andrzej"
print(uzytkownik_systemu)
uzytkownik_slownik = {"imie": "Michal", "nazwisko": "Zietkowski", "login": "michal123", "haslo": "haslo123"}
#metody pobierania danych ze słownika
print(uzytkownik_slownik["nazwisko"], uzytkownik_slownik["imie"])
#print(uzytkownik_slownik["adres_email"])
print(uzytkownik_slownik.get("adres_email"))
#metoda dodawania danych do słownika
uzytkownik_slownik["adres_email"] = "michalzietkowski@gmail.com"
print(uzytkownik_slownik)
#metoda zmiany wartosci w slowniku
uzytkownik_slownik["adres_email"] = "jan.kowalski@gmail.com"
print(uzytkownik_slownik)
#usuwanie danych ze slownikow
del(uzytkownik_slownik["adres_email"])
print(uzytkownik_slownik)

uzytkownik_slownik["adres_email"] = None

for klucz in uzytkownik_slownik.keys(): #tak samo jak bez tego keys
    print(klucz)

for wartosc in uzytkownik_slownik.values():
    print(wartosc)

for klucz, wartosc in uzytkownik_slownik.items():
    print(f"{klucz}: {wartosc}")
