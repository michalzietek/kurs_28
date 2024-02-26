class Trojkat:
    def __init__(self, podstawa, wysokosc):
        self.podstawa = podstawa
        self.wysokosc = wysokosc
        self.obwod = self.oblicz_obowod()
        self.pole = self.oblicz_pole()

    def oblicz_pole(self):
        return (self.podstawa * self.wysokosc)/2

    def oblicz_obowod(self):
        return None