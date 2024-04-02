import json

class FileHandler:
    def __init__(self, path_to_file):
        self.file = path_to_file
        self.data = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.file) as file:
            return json.loads(file.read())

    def save_data_to_file(self):
        with open(self.file, mode="w") as file:
            file.write(json.dumps(self.data))

    def upload_new_country_to_data(self, country_name, data):
        self.data[country_name] = data

    def __getitem__(self, item):
        return self.data.get(item)

    def __setitem__(self, key, value):
        self.data[key] = value

    def items(self):
        for country_key, country_data in self.data.items():
            yield f"{country_key}: {country_data}"

    def __iter__(self):
        return iter(self.data)
