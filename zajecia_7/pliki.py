import json
# file = open("imie.txt")
# for linia_pliku in file:
#     print(linia_pliku)
# data_pliku = file.read()
# print(data_pliku)
# file.close()

# with open("imie.txt", mode="r") as file:
#     print(file.read())
#
# with open("imie.txt", mode="w") as file:
#     file.write("Mariusz\n")
#
# with open("imie.txt", mode="a") as file:
#     file.write("Mateusz")
#
# with open("imie.txt", mode="r+") as file:
#     for imie in file:
#         print(imie)
#         if imie == "Mateusz":
#             file.write("Zietkowski")


with open("dane.txt", mode="a+") as file:
    file.write("Dane1")

with open("biblioteka.json") as file:
    biblioteka = json.loads(file.read())
    print(biblioteka)
    print(type(biblioteka))

