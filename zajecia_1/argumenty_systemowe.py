import sys
print(sys.argv)
print("argumenty systemowe")
print(sys.argv[1])
print(sys.argv[2])
folder_uzytkownika = sys.argv[1]
#kod do laczenia sie z google drive
google_drive.open(folder_uzytkownika)