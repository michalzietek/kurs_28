class Kwadrat:
    def __init__(self, bok):
        self.bok = bok
        self.obwod = self.oblicz_obowod()
        self.pole = self.oblicz_pole()

    def oblicz_pole(self):
        return self.bok ** 2

    def oblicz_obowod(self):
        return 4 * self.bok