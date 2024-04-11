from abc import ABC, abstractmethod

class Switchable(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("Wlaczylem swiatlo")

    def turn_off(self):
        print("Wylaczylem swiatlo")


class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        self.device.turn_on()

class TV(Switchable):
    def turn_on(self):
        print("Wlaczylem tv")

    def turn_off(self):
        print("Wylaczylem tv")



tv = TV()
light_bulb = LightBulb()
tv_switch = Switch(tv)
light_switch = Switch(light_bulb)
tv_switch.operate()
light_switch.operate()
lista = []