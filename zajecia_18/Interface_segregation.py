from abc import ABC, abstractmethod


class RobotDomowy(ABC):

    @abstractmethod
    def poscieraj_kurze(self):
        pass

    @abstractmethod
    def umyj_podloge(self):
        pass

    @abstractmethod
    def ugotuj_obiad(self):
        pass

    @abstractmethod
    def umyj_naczynia(self):
        pass


class RobotSprzatajacy(ABC):
    @abstractmethod
    def poscieraj_kurze(self):
        pass

    @abstractmethod
    def umyj_podloge(self):
        pass


class RobotKuchenny(ABC):
    @abstractmethod
    def ugotuj_obiad(self):
        pass

    @abstractmethod
    def umyj_naczynia(self):
        pass

class IRobotRumba(RobotSprzatajacy):
    def poscieraj_kurze(self):
        pass

    def umyj_podloge(self):
        pass

class Thermomix(RobotKuchenny):
    def ugotuj_obiad(self):
        pass

    def umyj_naczynia(self):
        pass