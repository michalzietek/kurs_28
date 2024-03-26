class StringKeysDictionary:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        if isinstance(key, str):
            self.data[key] = value
        else:
            print("Nie mozesz dodac wartosci z kluczem nietekstowym")

    def __getitem__(self, item):
        return self.data.get(item)

stringkeys = StringKeysDictionary()
stringkeys["Michal"] = "1"
stringkeys[1] = "1"
print(stringkeys.data)
