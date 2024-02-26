from math import pi
class Kolo:
    def __init__(self, promien):
        self.promien = promien
        self.obwod = self.oblicz_obowod()
        self.pole = self.oblicz_pole()

    def oblicz_pole(self):
        return pi * (self.promien ** 2)

    def oblicz_obowod(self):
        return 2 * pi * self.promien