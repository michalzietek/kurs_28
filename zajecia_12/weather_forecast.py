import requests
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="weather_forecast app")



user_date = input("Podaj datę sprawdzenia pogody: ")
user_city = input("Podaj miasto, dla którego chcesz sprawdzić pogodę: ")

def change_city_to_lattitude_and_longitude():
    location = geolocator.geocode(user_city)
    return (location.latitude, location.longitude)


latitude, longitude = change_city_to_lattitude_and_longitude()
print(latitude)
print(longitude)

url_address = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
               f"&hourly=rain&daily=rain_sum&timezone=Europe"
               f"%2FLondon&start_date={user_date}&end_date={user_date}")

weather_data_from_api = requests.get(url=url_address)

print(weather_data_from_api.status_code)
print(weather_data_from_api.json())
