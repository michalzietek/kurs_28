from enum import Enum


class Marki(Enum):
    AUDI = "mercedes"
    HYUNDAI = "hyundai"

twoja_marka = input("Podaj markę swojego samochodu: ")

if twoja_marka == Marki.AUDI.value:
    print("Masz audi")
elif twoja_marka == Marki.HYUNDAI.value:
    print("masz hyundaia")
else:
    print("Nie znam twojej marki")

czy_chcesz_serwis = bool(input("Czy chcesz serwisować swoje auto?"))

if czy_chcesz_serwis:
    if twoja_marka == Marki.AUDI.value:
        print("Idziesz do serwisu audi")
    elif twoja_marka == Marki.HYUNDAI.value:
        print("Idziesz do serwisu hyundai")
    else:
        print("Nie mamy twojego serwisu w bazie danych")
