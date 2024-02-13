# imie = input("Podaj swoje imie")
#
# print(f"Cześć, {imie}")
# print(f"Witajcie w szkole Future Collars")
# print("Cześć x2")

# wiek = int(input("Podaj mi swój wiek"))
# # if wiek >= 21:
# #     print(f"Pracujesz już {int(wiek) - 21}")
# # if wiek < 21:
# #     print("Nie powinieneś jeszcze pracować. Nie masz 21 lat")
#
# if wiek >= 21 and wiek < 65:
#     print(f"Pracujesz już {wiek - 21}")
# elif wiek < 21 and wiek > 0:
#     print("Nie powinieneś jeszcze pracować. Nie masz 21 lat.")
# elif wiek >= 65 and wiek < 120:
#     print("Nie powinieneś już pracować jesteś emerytem.")
# else:
#     print("Czy ty w ogóle jesteś człowiekiem?")


# 1 rok
# if wiek < 18:
#     print("Nie masz jeszcze 18 lat. Nie mogę Ci sprzedać napoju energetycznego")
#     wiek += 1
# else:
#     print("Masz już 18 lat. Oto twój napój energetyczny.")


# while <warunek, który musi zostać spełniony>:
#       kod do wykonania wewnątrz pętli
# print("Dzień dobry. Chciałabym kupić energetyka.")
# wiek = int(input("Podaj mi swój wiek "))
# while wiek < 18:
#     print("Nie masz jeszcze 18 lat. Nie mogę Ci sprzedać napoju energetycznego.")
#     print(f"Twój wiek to: {wiek}")
#     czy_chcesz_byc_pelnoletni = input("Czy chcesz dalej zostać dorosłym ")
#     if czy_chcesz_byc_pelnoletni == "nie":
#         break
#     czy_chcesz_zostac_w_tym_wieku = input("Czy chcesz zostać w tym wieku?")
#     if czy_chcesz_zostac_w_tym_wieku == "tak":
#         continue
#     # wiek = wiek + 1 to samo co wiek += 1
#     wiek += 1
# else:
#     print("Masz już ponad 18 lat.")


for nasza_nowa_zmienna in range(0, 10):
    print(nasza_nowa_zmienna)
    if nasza_nowa_zmienna == 7:
        break
    #print(type(nasza_nowa_zmienna))
#
# for litera in "abcd":
#     print(litera)
#     print(type(litera))