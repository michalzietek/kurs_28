uzytkownicy = [
    {
        "id": 1,
        "imie": "Michał",
        "nazwisko": "Zietkowski",
        "saldo": 1200
    },
    {
        "id": 2,
        "imie": "Jan",
        "nazwisko": "Kowalski",
        "saldo": 12000
    }
]

print("Witaj w programie bankowym.")
print("Co chcesz zrobić?")
rodzaj_operacji = input("1. Przelew\n2. Wypłata gotówki\n3. Wpłata gotówki\n")
if rodzaj_operacji == "1":
    pierwszy_uzytkownik = int(input("Podaj id użytkownika zlecającego przelew "))
    drugi_uzytkownik = int(input("Podaj id użytkownika, do którego przelew ma być wysłany "))
    kwota = float(input("Podaj kwotę"))
    for uzytkownik in uzytkownicy:
        if uzytkownik.get("id") == pierwszy_uzytkownik:
            uzytkownik_zlecajacy = uzytkownik
        if uzytkownik.get("id") == drugi_uzytkownik:
            uzytkownik_otrzymujacy = uzytkownik
    if uzytkownik_zlecajacy.get("saldo") >= kwota:
        uzytkownik_zlecajacy["saldo"] -= kwota
        uzytkownik_otrzymujacy["saldo"] += kwota
    else:
        print("Niestety nie masz takiej gotówki")
    print(uzytkownik_zlecajacy)
    print(uzytkownik_otrzymujacy)