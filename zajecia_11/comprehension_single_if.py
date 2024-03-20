
# age = int(input("Podaj mi swój wiek"))
# # is_adult = False
# # if age >= 18:
# #     is_adult = True
# # else:
# #     is_adult = False
#
# # is_adult = True if age >= 18 else False
# #
# # print("Jesteś dorosły") if is_adult else print("Nie masz 18 lat.")
#
# print("Jesteś dorosły") if age >= 18 else print("Nie masz 18 lat.")


# if is_adult:
#     print("Jesteś dorosły")
# else:
#     print("Nie masz jeszcze 18 lat.")

family_list = ["Jan", "maciej", "Konrad", "Maria", "zosIA"]
print(family_list)
# correct_family_list = []
# for family_member in family_list:
#     correct_family_list.append(family_member.capitalize())
#
# print(correct_family_list)

correct_family_list_comprehension = [family_member.capitalize() for family_member in family_list]

males_in_family = []
for family_member in family_list:
    if family_member[-1].lower() != "a":
        males_in_family.append(family_member.capitalize())

males_in_family_comprehension = [family_member.capitalize() for family_member in family_list if family_member[-1].lower() != "a"]

family_members_and_indexes = {index: family_member.capitalize() for index, family_member in enumerate(family_list)}

print(family_members_and_indexes)

print(males_in_family_comprehension)
print(males_in_family)
# [to co chcemy dodać do tej listy for tymczasowa_zmienna in struktura_iterowalna]

# print(correct_family_list_comprehension)
