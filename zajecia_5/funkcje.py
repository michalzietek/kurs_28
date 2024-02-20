# def wywolaj_imie(imie):
#     print(f"Witaj {imie}")
# wywolaj_imie("Jan")
# wywolaj_imie("Konrad")
# wywolaj_imie("Jacek")
# nowe_imie = input("Podaj nowe imie: ")
# wywolaj_imie(nowe_imie)
emerytura = 1000
def oblicz_moja_emeryture(pensja=10, typ_zawodu="programista"):
    if typ_zawodu == "programista":
         emerytura = pensja * 0.001
    elif typ_zawodu == "policjant":
         emerytura = pensja * 0.80
    else:
         emerytura = pensja * 0.5
    return emerytura

typ_zawodu_input = input("Podaj typ swojego zawodu: ")
pensja_input = input("Podaj swoją pensję: ")
emerytura_wywolanie = oblicz_moja_emeryture(float(pensja_input), typ_zawodu_input)
nowa_emerytura = oblicz_moja_emeryture(pensja=6000000, typ_zawodu=typ_zawodu_input)
trzynastka = oblicz_moja_emeryture(40000)
dummy_emerytura = oblicz_moja_emeryture()
print(dummy_emerytura)
#oblicz_moja_emeryture(float(pensja_input),typ_zawodu_input)
print(f"Twoja emerytura wynosi: {emerytura_wywolanie}")
print(f"Twoja nowa emerytura wynosi: {nowa_emerytura}")
print(f"Trzynastka wynosi: {trzynastka}")