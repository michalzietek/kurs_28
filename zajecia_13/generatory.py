def wyprintuj_wszyskie_numery_z_listy(lista):
    for numer in lista:
        print(numer)

def zwroc_wszystkie_numery_parzyste_z_zakresu(lista):
    numery_parzyste = []
    for index, numer in enumerate(lista):
        numery_parzyste.append(numer) if index % 2 == 0 else None
    return numery_parzyste

def zwroc_kolejne_liczby_parzyste_z_zakresu(lista):
    for index, numer in enumerate(lista):
        return numer if index % 2 == 0 else None

kolejny_numer_parzysty = zwroc_kolejne_liczby_parzyste_z_zakresu(range(100))
# print(kolejny_numer_parzysty)
# print(kolejny_numer_parzysty)
# print(kolejny_numer_parzysty)
# print(kolejny_numer_parzysty)

def zwroc_kolejne_liczby_parzyste_z_zakresu_generator(lista):
    for index, numer in enumerate(lista):
        if index % 2 == 0:
            yield numer

kolejny_numer_parzysty_generator = zwroc_kolejne_liczby_parzyste_z_zakresu_generator(range(100))

for numer in kolejny_numer_parzysty_generator:
    print(numer)
