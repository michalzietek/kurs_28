"""
Jesteś odpowiedzialny za napisanie programu do obsługi kasy w sklepie typu Żabka. Program ma na celu przeprowadzenie klienta przez proces płacenia za zakupy, z ograniczeniem do 100 zł na jedną transakcję oraz walidacją wieku klienta dla określonych produktów (alkohol, papierosy, napoje energetyczne).

co jak bedziemy chcieli kupic cos na co jestesmy za mlodzi?
odrzucamy produkt i wtedy kontynuujemy zakupy

**Na zakończenie działania programu należy wyświetlić:**
1. Wartość zakupów we wszystkich transakcjach.
2. Informację o tym, czy klient chciał kupić produkt nieodpowiedni dla swojego wieku.
3. Transakcję z największą kwotą


1. Czego my będziemy wymagali od klienta Żabki?
- wiek
- rodzaj każdego produktu
- cena
- czy produkt jest dla pelnoletnich? (tutaj nie musimy tego definiować na początku)
- ilość produktów w koszyku


2. Co my będziemy musieli klientowi wyświetlić na końcu?
- Kwota do zapłaty
- Ilość transakcji
- Informację o tym, czy klient chciał kupić produkt nieodpowiedni dla swojego wieku.
- Transakcję z największą kwotą

3. Co nasz program będzie musiał robić?
- Musi dodawać produkty do rachunku klienta (skanowanie jak przy kasie)
- Musi zapamiętywać ilość transakcji dokonanych przez klienta
- Musi pamiętać, która transakcja była najwyższa i jej kwotę
- Musi sprawdzać czy produkt jest dozwolony czy nie
- Wyświetlić podsumowanie


"""
print("Witaj w sklepie Żabka.")

wiek = int(input("Podaj mi swój wiek: "))
ilosc_produktow_w_koszyku = int(input("Podaj mi ilość produktów w koszyku: "))
suma_rachunku = 0
liczba_transakcji = 1
suma_w_transakcji = 0
kwota_najwiekszej_transakcji = 0
numer_najwiekszej_transakcji = 1
'''
range(liczba_poczatkowa, liczba_koncowa, skok)
range(0, 4)
[0 , 1, 2, 3]
range(5)
[0, 1, 2, 3, 4]
range(1, 7, 2)
[1, 3, 5]
'''
for numer_produktu in range(ilosc_produktow_w_koszyku):
    rodzaj_produktu = input(f"Podaj typ produktu {numer_produktu +1}: ")
    cena_produktu = float(input(f"Podaj cenę produktu {numer_produktu +1}: "))
    if wiek < 18 and (rodzaj_produktu.lower() == "alkohol" or rodzaj_produktu.upper() == "PAPIEROSY" or rodzaj_produktu.capitalize() == "Energetyk"):
        print("Produkt niedozwolony dla twojego wieku")
        continue
    if cena_produktu > 100:
        print("Niestety nie mamy takich produktów na stanie")
        continue
    suma_rachunku += cena_produktu
    if suma_w_transakcji + cena_produktu <= 100:
        suma_w_transakcji += cena_produktu
    else:
        if suma_w_transakcji >= kwota_najwiekszej_transakcji:
            kwota_najwiekszej_transakcji = suma_w_transakcji
            numer_najwiekszej_transakcji = liczba_transakcji
        liczba_transakcji += 1
        # suma_w_transakcji = 0
        # suma_w_transakcji += cena_produktu
        suma_w_transakcji = cena_produktu

if liczba_transakcji == 1:
    if suma_rachunku == 0:
        liczba_transakcji = 0
    kwota_najwiekszej_transakcji = suma_w_transakcji
    numer_najwiekszej_transakcji = liczba_transakcji

'''
numer_produktu = 0

while numer_produktu < ilosc_produktow_w_koszyku:
    numer_produktu += 1
'''
if liczba_transakcji != 0:
    print(f"Suma twojego rachunku wynosi: {suma_rachunku}")
    print(f"Ilość transakcji wynosi: {liczba_transakcji}")
    print(f"Kwota największej transakcji: {kwota_najwiekszej_transakcji}")
    print(f"Numer największej transakcji: {numer_najwiekszej_transakcji}")
else:
    print("Niestety nie udało Ci się dokonać zakupu")
