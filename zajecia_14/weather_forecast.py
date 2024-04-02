import json

class WeatherForecast:
    def __init__(self, path_to_file):
        self.file = path_to_file
        self.data = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.file) as file:
            return json.loads(file.read())

    def save_data_to_file(self):
        with open(self.file, mode="w") as file:
            file.write(json.dumps(self.data))

    def __getitem__(self, item):
        city, date = item
        print(city)
        print(date)
        selected_city = self.data.get(city)
        if selected_city:
            for city_date, info in selected_city.items():
                if city_date == date:
                    return info
        return None

    def __setitem__(self, key, value):
        city, date = key
        city_data = self.data.get("city")
        if city_data:
            self.data[city][date] = value
        else:
            self.data[city] = {}
            self.data[city][date] = value

    def items(self):
        #tutaj musimy zrobic petle w petli i dopiero yieldowac
        pass


weather_forecast = WeatherForecast(path_to_file="weather_data.json")
print(weather_forecast.data)
print(weather_forecast[("Szczecin", "2024-03-22")])
weather_forecast[("Zakopane", "2024-03-28")] = "nie pada"
weather_forecast[("Zakopane","2024-03-28")]
weather_forecast.save_data_to_file()
