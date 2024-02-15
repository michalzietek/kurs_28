imie = "Michal"
print(id(imie))
lista_michala = [imie, "Zietkowski", 18] #gorszy sposob
lista_michala_20 = ["Michal", "Zietkowski", 18] #lepszy sposob
print(lista_michala)
imie = "Andrzej"
lista_michala[0] = "Artur"
print(imie)
print(lista_michala)
# for item in lista_michala:
#     print(id(item))
# print(id(imie))
# print(lista_michala)
# my_tuple = (1, 2, 3)
# print(id(my_tuple))
# my_tuple = (3, 4, 5)
# print(id(my_tuple))
# print("-----------------------------------")
# print(id(lista_michala))
# lista_michala.append("abcdefgh")
# print(id(lista_michala))