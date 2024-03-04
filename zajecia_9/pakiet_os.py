import os

obecny_folder = os.getcwd()
print(obecny_folder)
#os.mkdir("nowy_folder")
os.chdir("/home/michal/future_collars/kurs_28")
pliki = os.listdir(obecny_folder)
#os.mkdir("zajecia_10")
pliki2 = os.listdir()
for plik in pliki:
    print(os.path)
    if os.path.isfile(plik):
        print("Mamy plik")
        print(plik)
    else:
        print("Nie mamy pliku")