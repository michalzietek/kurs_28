"""
Stwórz system zarządzania księgozbiorem bibliotecznym, który pozwoli na monitorowanie przepływu książek oraz śledzenie budżetu biblioteki.
Po uruchomieniu systemu użytkownik otrzymuje listę komend do wyboru:
- doładowanie
- wypożycz
- zakup
- bieżący_stan
- zestawienie
- szczegóły_książki
- dziennik
- zakończ
Funkcje po wywołaniu danych komend są następujące:
1. doładowanie - Umożliwia dodanie środków do budżetu biblioteki lub ich odjęcie.
2. wypożycz - Rejestruje wypożyczenie książki przez czytelnika. System żąda podania tytułu, opłaty za wypożyczenie i liczby dni. Koszt wypożyczenia jest dodawany do budżetu.
3. zakup - Rejestruje zakup nowych książek dla biblioteki. System pyta o tytuł książki, koszt zakupu i liczbę egzemplarzy. Zakupione książki są dodawane do zbioru, a środki są odprowadzane z budżetu, który nie może być negatywny po transakcji.
4. bieżący_stan - Wyświetla aktualny stan środków finansowych.
5. zestawienie - Podsumowuje cały księgozbiór biblioteki wraz z cenami zakupu i ich ilością.
6. szczegóły_książki - Wyświetla dostępność i dane dotyczące pojedynczej książki po wpisaniu jej tytułu.
7. dziennik - Przegląd historii transakcji. Podając wartości "od" i "do", system wyświetla zapisane działania w podanym zakresie. W przypadku pustych pól lub wartości spoza zakresu, użytkownik jest informowany o błędzie i wyświetlana jest liczba wszystkich zarejestrowanych transakcji.
8. zakończ - Kończy działanie programu.
**Inne wymagania:**
- System działa do momentu wybrania komendy zakończ.
- Operacje doładowanie, wypożycz oraz zakup są zapisywane dla późniejszej referencji przy użyciu komendy dziennik.
- Po każdej komendzie system wyświetla ponownie listę dostępnych opcji i prosi o wybór kolejnej.
- Ochrona przed błędami użytkownika, takimi jak wpisywanie błędnych danych czy żądanie zakupu na wartości ujemne. Powinno być również sprawdzanie poprawności typów danych wprowadzanych przez użytkownika.
"""
budzet_ksiegarni = 10000.0
ksiegozbior = [
    {
        "tytul": "Wiedzmin",
        "autor": "Andrzej Sapkowski",
        "wydawnictwo": "Supernowa",
        "gatunek": "Fantasy",
        "ilosc_sztuk": 5,
        "ilosc_dostepnych_sztuk": 3

    }
]
lista_operacji = []
koniec_programu = False
print("Witaj w naszej biliotece!")
while not koniec_programu:
    operacja = input("Wybierz co chcesz zrobić:\n1. Doładowanie\n2. Wypożycz książkę\n3. Zakup\n4. Bieżący stan\n5. Zestawienie"
                    "\n6. Szczegóły ksiązki\n7. Dziennik\n8. Zakończ program\n")

    if operacja == "1":
        kwota_do_dodania = input("Podaj kwotę do dodania: ")
        budzet_ksiegarni += float(kwota_do_dodania)
        lista_operacji.append(f"Zmieniono budżet o {kwota_do_dodania}")
        if float(kwota_do_dodania) < 0:
            print("Uważaj, bo odjąłeś środki. Czy nie jesteś złodziejem?")
    elif operacja == "2":
        autor_ksiazki = input("Popros o autora książki: ")
        nazwa_książki = input("Popros o tytuł ksiązki: ")
        znaleziono_ksiazke = False
        wypozyczono_ksiazke = False
        for ksiazka in ksiegozbior:
            if ksiazka.get("tytul") == nazwa_książki and ksiazka.get("autor") == autor_ksiazki:
                znaleziono_ksiazke = True
                if ksiazka.get("ilosc_dostepnych_sztuk") > 0:
                    ksiazka["ilosc_dostepnych_sztuk"] -= 1
                    wypozyczono_ksiazke = True
        if wypozyczono_ksiazke:
            budzet_ksiegarni += 15
            lista_operacji.append(f"Wypozyczono książkę {nazwa_książki}")
        elif znaleziono_ksiazke and not wypozyczono_ksiazke:
            print("Niestety ta książka nie jest dostępna")
            lista_operacji.append(f"Próba wypożyczenia {nazwa_książki}, brak dostępności")
        else:
            print("Nie posiadamy takiej książki")
            lista_operacji.append("Próba wypożyczenia książki, której nie mamy")
    elif operacja == "3":
        tytul = input("Podaj tytuł książki, którą chcesz kupić: ")
        autor = input("Podaj autora książki: ")
        wydawnictwo = input("Podaj wydawnictwo: ")
        gatunek = input("Podaj gatunek książki: ")
        ilosc_sztuk = int(input("Podaj ilość, jaką chcesz kupić: "))
        cena_jednostkowa = float(input("Podaj cenę jednostkową książki: "))
        if budzet_ksiegarni >= ilosc_sztuk * cena_jednostkowa:
            ksiegozbior.append({
                "tytul": tytul,
                "autor": autor,
                "wydawnictwo": wydawnictwo,
                "gatunek": gatunek,
                "ilosc_sztuk": ilosc_sztuk,
                "ilosc_dostepnych_sztuk": ilosc_sztuk
            })
            budzet_ksiegarni = budzet_ksiegarni - (ilosc_sztuk * cena_jednostkowa)
        else:
            print(f"Niestety, nie stać nas na zakup tych pozycji. Twój budżet to: {budzet_ksiegarni}")
    elif operacja == "4":
        print(f"Twój budżet wynosi: {budzet_ksiegarni}")
    elif operacja == "5":
        print(ksiegozbior)
    elif operacja == "7":
        od = input("Podaj mi początkowy zakres: ")
        do = input("Podaj mi końcowy zakres: ")
        if od != "" and do != "":
            print(lista_operacji[int(od):int(do)])
        elif od != "" and do == "":
            print(lista_operacji[int(od):])
    elif operacja == "8":
        koniec_programu = True