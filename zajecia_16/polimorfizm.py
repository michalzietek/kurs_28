from math import pi

class Figura:
    def oblicz_pole(self):
        pass

class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok

    def oblicz_pole(self):
        return self.bok ** 2


class Kolo(Figura):

    def __init__(self, promien):
        self.promien = promien

    def oblicz_pole(self):
        return pi * self.promien ** 2


kwadrat = Kwadrat(bok=4)
kolo = Kolo(promien=2)
for figura in (kwadrat, kolo):
    print(figura.oblicz_pole())
