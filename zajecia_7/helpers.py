from figury.kolo import Kolo
from figury.kwadrat import Kwadrat
def oblicz_dane_figury(figura):
    if figura == "kolo":
        promien = int(input("Podaj promien kola: "))
        kolo = Kolo(promien=promien)
        print(kolo.pole)
        print(kolo.obwod)
    elif figura == "kwadrat":
        bok = input("Podaj bok kwadratu: ")
        kwadrat = Kwadrat(bok=bok)
        print(kwadrat.pole)
        print(kwadrat.obwod)
    else:
        print("Nie ma takiej figury")
