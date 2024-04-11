from abc import ABC, abstractmethod
#
# class UserInterface(ABC):
#
#     @abstractmethod
#     def save(self):
#         pass
#
#     @abstractmethod
#     def get_user(self):
#         pass
#
#
# user = UserInterface()
#
# class BaseUser(UserInterface):
#     def save(self):
#         pass
#
#     def get_user(self):
#         pass
#
# class SuperUser(UserInterface):
#     def save(self):
#         pass
#
#     def get_user(self):
#         pass

class Ptak(ABC):
    pass


class LatajacyPtak(Ptak):
    @abstractmethod
    def lec(self):
        pass


class Skowronek(LatajacyPtak):
    def lec(self):
        print("Ja latam")


class Strus(Ptak):
    pass

strus = Strus()
strus.lec()