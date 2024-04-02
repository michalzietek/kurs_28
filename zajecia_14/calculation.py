def dodawanie(a, b):
    return a + b


def sprawdz_moja_emeryture(wiek):
    if wiek >= 65:
        return 4000
    if 18 < wiek < 65:
        return 1200
    else:
        return 0