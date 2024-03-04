import math
from decimal import Decimal

kwota_1 = 1234545.05
kwota_2 = Decimal(1234545.05)

operacja = 10/3
print(round(operacja, 2))
print(math.floor(operacja))
print(f"Do twojego konta doszło - {operacja - math.floor(operacja)}")
twoje_oceny = [1, 2, 4, 5, 3, 6, 4, 5]
suma_ocen = 0
for ocena in twoje_oceny:
    suma_ocen += ocena
suma_ocen_1 = math.fsum(twoje_oceny)
print(math.fabs(suma_ocen))


print(suma_ocen/len(twoje_oceny))
print(suma_ocen_1/len(twoje_oceny))