class BazaSzkolna:
    def __init__(self, baza_szkoly):
        self.baza_szkoly = baza_szkoly

    def __repr__(self):
        return f"Szkoła: {self.baza_szkoly}"

    def __setitem__(self, key, value):
        self.baza_szkoly[key] = value

    def __getitem__(self, item):
        return self.baza_szkoly.get(item)



szkola = {
    "1a": ["Michal Zietkowski", "Jacek Kurski"],
    "2a": ["Jan Nowak", "Donald Trump"]
}

baza_szkolna = BazaSzkolna(szkola)
baza_szkolna.baza_szkoly["3a"] = ["Dawid Ziobro", "Robert Lewandowski"]
baza_szkolna["4a"] = ["Piotr Zielinski", "Wojciech Szczesny"]
print(baza_szkolna["4a"])
print(baza_szkolna.baza_szkoly["4a"])
print(baza_szkolna.baza_szkoly.get("4a"))
print(baza_szkolna)
