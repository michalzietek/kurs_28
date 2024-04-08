from math import pi
from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def oblicz_pole(self):
        raise NotImplementedError("Nie masz zaimplementowanej metody do obliczenia pola")

    @abstractmethod
    def oblicz_obwod(self):
        raise NotImplementedError("Nie masz zaimplementowanej metody do obliczenia obwodu")


class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok

    def oblicz_pole(self):
        return self.bok ** 2

    def oblicz_obwod(self):
        print("hehehe")


class Kolo(Figura):

    def __init__(self, promien):
        self.promien = promien

    def oblicz_pole(self):
        return pi * self.promien ** 2

    def oblicz_obwod(self):
        print("kolo kolo")


kwadrat = Kwadrat(bok=10)
kolo = Kolo(promien=5)