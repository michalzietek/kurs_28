def oblicz_sume_danych(lista_danych):
    suma = 0
    for numer in lista_danych:
        suma+=numer
    return suma

suma_danych = oblicz_sume_danych([1, 2, 20, 5452345, 363635, 32525545, 533654545454])
print(suma_danych)

def oblicz_sume_danych_bez_listy(pierwsza_liczba, druga_liczba, trzecia_liczba, czwarta_liczba):
    suma = pierwsza_liczba + druga_liczba + trzecia_liczba + czwarta_liczba
    return suma

suma_2 = oblicz_sume_danych_bez_listy(1, 2, 3, 4)
print(suma_2)

def oblicz_sume_danych_z_args(*args):
    suma = 0
    for liczba in args:
        suma+=liczba
    return suma

def oblicz_sume_danych(lista_danych):
    suma = 0
    for numer in lista_danych:
        suma+=numer
    return suma

suma_danych = oblicz_sume_danych([1, 2, 20, 5452345, 363635, 32525545, 533654545454])
print(suma_danych)
suma_z_args = oblicz_sume_danych_z_args(1, 2, 3, 4, 5, 5646474, 63563466, 56474747, 4574765785, 56875858575)
print(suma_z_args)

def polacz_sie_z_baza_danych(**kwargs):
    if "url" in kwargs.keys():
        print("polaczona za pomoca url")
    else:
        print("polaczono za pomoca hosta")

def polacz_z_baza_danych_normalnie(url=None, admin=None, data=None, haslo=None):
    if url:
        print("polaczona za pomoca url")
    else:
        print("polaczono za pomoca hosta")

polacz_z_baza_danych_normalnie(url="www.host.pl")
polacz_z_baza_danych_normalnie(admin="michal")
polacz_sie_z_baza_danych(url="www.host.pl", admin="123", data="29.02.2024", haslo="1234", dupa="dupa")

def przywitaj_sie(imie, *args, **kwargs):
    print(f"Cześć {imie}")

przywitaj_sie("Michał", "Kuba", "Jacek", "Maciek", nazwisko="Ziętkowski")

