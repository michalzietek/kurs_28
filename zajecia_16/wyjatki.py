lista_osob = ["Michal", "Tomek", "Atomek"]
try:
    wiek = input("Podaj mi swój wiek")
    int(wiek)
    # print(lista_osob[3])
    # print(lista_osob[1])
    # lista_osob[4] = "Romek"
except IndexError:
    print("Lista jest za długa")
    #Wyswietlamy bledy uzytkownikowi
except ValueError:
    print("To nie jest wartość numeryczna")
# except (IndexError, ValueError):
#     pass
finally:
    print("Jestesmy w finally")

print("hehe przeszedlem dalej")


