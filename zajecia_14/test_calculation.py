from calculation import dodawanie, sprawdz_moja_emeryture


def test_dodawanie():
    wynik = dodawanie(2, 2)
    wynik2 = dodawanie(2, 3)
    assert wynik == 4
    assert wynik2 == 5

def test_sprawdz_moja_emeryture_dla_wieku_powyzej_65_lat():
    assert sprawdz_moja_emeryture(70) == 4000

def test_sprawdz_moja_emeryture_dla_wieku_produkcyjnego():
    assert sprawdz_moja_emeryture(45) == 1200

def test_sprawdz_moja_emeryture_dla_niepelnoletnich():
    assert sprawdz_moja_emeryture(12) == 0

