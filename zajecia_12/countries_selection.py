"""
**Zadanie: Napisz program, który dostarczy informacji o wybranym kraju. Użyj do tego poniższego API Rest Countries. Aplikacja ma działać następująco:**
• Program pyta użytkownika o nazwę kraju, dla którego należy sprawdzić informacje. Nazwa kraju musi być podana w języku angielskim i pozwala na pełne lub częściowe dopasowanie.
• Aplikacja wykona zapytanie do API w celu pozyskania danych o kraju.
• Program powinien wyświetlić następujące informacje o kraju (jeżeli są dostępne):
    ◦ Pełna nazwa kraju
    ◦ Stolica
    ◦ Region
    ◦ Podregion
    ◦ Populacja
    ◦ Języki urzędowe
    ◦ Waluta
    ◦ Flagę (poprzez URL do obrazka)
• Wyniki zapytań powinny być zapisywane do pliku. Jeżeli szukany kraj znajduje się już w pliku, nie wykonuj zapytania do API, tylko zwróć wynik z pliku.
URL do API:
https://restcountries.com/v3.1/name/{country_name}?fullText=true
W URL należy uzupełnić parametr: country_name
Przykładowy funkcjonalny rezultat dla zapytania "Poland":
Pełna nazwa: Republic of Poland
Stolica: Warsaw
Region: Europe
Podregion: Eastern Europe
Populacja: 37970000
Języki urzędowe: Polish
Waluta: Polish złoty (PLN)
Flaga: https://flagcdn.com/pl.svg
**Wskazówka:** Możesz wymagać od użytkownika podania pełnej nazwy kraju (ustawiając parametr fullText na true w URL) lub pozwolić na wyszukiwanie zarówno pełnych, jak i częściowych nazw kraju (bez parametru fullText).
"""

from file_handler import FileHandler
from utils import retrieve_data_from_api, get_data_from_file

file_handler = FileHandler("countries_data.json")

print(file_handler.data)

user_country = input("Please type in country you want to find out more about: ")
country_in_file = get_data_from_file(file_handler.data, user_country)
if country_in_file:
    print(country_in_file)
    print("Pobrano dane z pliku")
else:
    print("Pobrano dane z API")
    data_from_api = retrieve_data_from_api(user_country)
    file_handler.upload_new_country_to_data(user_country, data_from_api)
    file_handler.save_data_to_file()
print(user_country)