Towary_magazynowe = [
    {
        "Nazwa_towaru": "Rura",
        "Cena_towaru": 5.60,
        "Ilosć": 3
    }
]
budżet_magazynu = 1000
lista_działań = []
koniec = False
print ("\n Program magazynowy MAG1\n Wybierz co chcesz zrobić:  \n")
while not koniec:
    działanie = input("\n 1-Saldo\n 2-Sprzedaż\n 3-Zakup\n 4-Konto\n 5-Lista\n 6-Magazyn\n 7-Przegląd\n 8-Wyjscie\n ")
    if działanie == ("1"):
        wartosć_dodania_do_budżetu= int(input ("Podaj wartosć zwiększenia/zmniejszenia budżetu magazynu: "))
        budżet_magazynu += wartosć_dodania_do_budżetu
        print (f"\nWartosc konta po zmianie wynosi {budżet_magazynu}")
        lista_działań.append(f"Dodano/zdjęto z konta magazynu  {wartosć_dodania_do_budżetu}")
        print (lista_działań)
    elif działanie == "2":
        nazwa_towaru_do_kupienia=input("Podaj nazwę towaru, który chcesz sprzedać: ")
        ilosć_do_kupienia = int(input("Podaj ilosć towaru: "))
        for towar in Towary_magazynowe:
            if towar.get ("Nazwa_towaru") == nazwa_towaru_do_kupienia and towar.get("Ilosć") < ilosć_do_kupienia:
                print(f"Nie mamy wystarczającej ilosći towaru, obecnie na stanie jest {(towar.get('Ilosć'))} szt.\n")
                lista_działań.append(f"Próba sprzedaż towaru {nazwa_towaru_do_kupienia} w większej ilosci niż jest na stanie")
            if towar.get ("Nazwa_towaru") == nazwa_towaru_do_kupienia and towar.get ("Ilosć") >= ilosć_do_kupienia:
                print ("Towar dodany do koszyka\n")
                budżet_magazynu += ilosć_do_kupienia * towar.get ("Cena_towaru")
                nowa_ilosć=towar.get("Ilosć") - ilosć_do_kupienia
                Towary_magazynowe.append({"Ilosć":nowa_ilosć})
                lista_działań.append(f"Sprzedano towar {nazwa_towaru_do_kupienia} w ilosci {ilosć_do_kupienia} szt.")
            else:
                print("Nie mamy takiego towaru\n")
                lista_działań.append(f"Próba sprzedaży towaru {nazwa_towaru_do_kupienia} którego nie ma na stanie")
    elif działanie == "3":
        Nazwa_towaru = input("Podaj nazwę towaru, który chcesz wprowadzić na magazyn: ")
        Cena_towaru = float(input("Podaj cenę jednostkową towaru: "))
        Ilosć_towaru = int(input ("Podaj ilosć towaru: "))
        if Cena_towaru * Ilosć_towaru > budżet_magazynu:
            print ("\nWartosć towarów przekracza budżet magazynu, zakup nie jest możliwy\n ")
            lista_działań.append(f"Próba zakupu towaru {Nazwa_towaru} o wartosci transakcji większej niż budżet magazynu")
        elif Cena_towaru * Ilosć_towaru <= budżet_magazynu:
            Towary_magazynowe.append({"Nazwa_towaru":Nazwa_towaru,"Cena_towaru":Cena_towaru,"Ilosć":Ilosć_towaru})
            lista_działań.append(f"Zakupiono towar {Nazwa_towaru} w ilosci {Ilosć_towaru} szt. za łączną wartosć {Cena_towaru*Ilosć_towaru}")
            print(f"Zakupiono towar {Nazwa_towaru} w ilosci {Ilosć_towaru} szt. za łączną wartosć {Cena_towaru*Ilosć_towaru}")
    elif działanie == "4":
        print(f"Wartosc konta wynosi: {budżet_magazynu}\n")
        lista_działań.append(f"Sprawdzono wartosć konta, która wyniosła {budżet_magazynu}")
    elif działanie == "5":
        print (Towary_magazynowe)
        lista_działań.append(f"Sprawdzono stan magazynowy towarów")
    elif działanie == "6":
        towar_do_wyswietlenia = input("Podaj nazwę towaru, którego chcesz sprawdzić ilosć: \n")
        for towar in Towary_magazynowe:
            if towar.get("Nazwa_towaru") == towar_do_wyswietlenia:
                print (f"Obecnie na stanie jest {(towar.get('Ilosć'))} szt. towaru {towar_do_wyswietlenia}")
                lista_działań.append(f"Sprawdzono stan towaru {towar_do_wyswietlenia}, którego ilosć wyniosła {(towar.get('Ilosć'))} szt.")
                break
            else:
                #to jest niepotrzebne
                print ("Nie mamy takiego towaru na stanie")
                lista_działań.append(f"Próba podanie stanu magazynowego towaru {towar_do_wyswietlenia} którego ne było na stanie magazynowym")
    elif działanie == "7":
        od = input("Podaj początkowy zakres akcji: ")
        do = input ("Podaj końcowy zakres akcji: ")
        if od =="" and do == "":
            print(lista_działań)
        elif od !="" and do == "":
            print (lista_działań[int(od):])
        elif od =="" and do != "":
            print (lista_działań)
        elif len(lista_działań) < int(do):
            print (f"Wartosc poza zakresem, wybierz od 0 do {len (lista_działań)-1}")
        elif int(do)>= 0 and int(do)>=0:
            print ((lista_działań) [int(od):int(do)+1])
    elif działanie == "8":
        koniec = True