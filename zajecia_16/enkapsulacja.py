class KontoBankowe:
    
    def __init__(self, saldo_poczatkowe):
        self.__saldo = saldo_poczatkowe



    def get_saldo(self):
        return self.__saldo

    def zmien_saldo(self, nowy_stan):
        self.__saldo = nowy_stan


konto_bankowe_michala = KontoBankowe(saldo_poczatkowe=1000)
konto_bankowe_michala.get_saldo()
konto_bankowe_michala.zmien_saldo(50)
konto_bankowe_michala.__saldo = 100
print(id(konto_bankowe_michala.get_saldo()))
print(id(konto_bankowe_michala.__saldo))