from file_handler import FileHandler

class Manager:
    def __init__(self):
        self.instancja_file_handlera = FileHandler(sciezka_do_pliku_z_historia="historia.json",
                                              sciezka_do_pliku_z_ksiegozbiorem_i_saldem="ksiegozbior_i_saldo.json")

        self.budzet_ksiegarni, self.ksiegozbior = self.instancja_file_handlera.odczyt_danych_z_pliku_z_ksiegozbiorem_i_saldem()
        self.lista_operacji = self.instancja_file_handlera.odczyt_danych_z_pliku_z_historia()
        self.actions = {}

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb

        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self)


manager = Manager()
