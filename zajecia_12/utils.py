import requests


def retrieve_data_from_api(country):
    url_address = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url_address)
    print(response.status_code)
    if response.status_code == 200:
        print("Hura udało się, pobieramy dane do naszego programu")
        return load_data_from_api_response_to_dict(response.json())
    else:
        print("Niestety nie ma takiego kraju, lub pobranie danych się nie powiodło.")


def load_data_from_api_response_to_dict(api_response_data):
    print(api_response_data)
    country_from_list = api_response_data[0]
    return {
        "name": country_from_list.get("name").get("official"),
        "capital": country_from_list.get("capital"),
        "region": country_from_list.get("region"),
        "population": country_from_list.get("population"),
        "languages": country_from_list.get("languages"),
        "currency": country_from_list.get("currencies")

    }


def get_data_from_file(data, country):
    for key, value in data.items():
        if key == country:
            return value
    return None