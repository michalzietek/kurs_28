# adres_email = "michalzietkowski@gmail.com"
# def zwaliduj_adres_email(email):
#     if "@" in email:
#         print("poprawny adres email")
#     else:
#         print("Nipepoprawny adres email")
#
#
# zwaliduj_adres_email(adres_email)
# zwaliduj_adres_email("1@michalzietkowski2.com")
# zwaliduj_adres_email("com.gmail@michalzietkowski")

import re

pattern = r'^[\S]+@[\w]+.[\S]{2,}$'
adres_email = "michalzietkowski@gmail.com"

def match_email(email):
    if re.match(pattern, email):
        return True
    return False

check = match_email(adres_email)
check2 = match_email("11111@a")
check3 = match_email("111 11@gmail.com")
print(check)
print(check2)
print(check3)
