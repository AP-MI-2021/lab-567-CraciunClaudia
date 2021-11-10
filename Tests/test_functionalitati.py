from Domain.Cheltuiala import creeaza_cheltuiala, get_id, get_suma
from Logic.functionalitati import stergere_cheltuieli, adauga_valoare, cea_mai_mare_cheltuiala, ordonare_descrescatoare, \
    sume_lunare

lst_cheltuieli = [
    creeaza_cheltuiala(22, 145, "25.06.2021", "alte cheltuieli", 1),
    creeaza_cheltuiala(12, 348, "25.06.2021", "canal", 2),
    creeaza_cheltuiala(22, 165, "20.01.2019", "întreținere", 3),
    creeaza_cheltuiala(22, 200, "13.12.2018", "întreținere", 4),
]


def test_stergere_cheltuieli():
    lista = lst_cheltuieli
    lista = stergere_cheltuieli(22, lista)
    assert len(lista) == 1
    assert get_id(1) is None
    assert get_id(3) is None
    assert get_id(4) is None

    lista = lst_cheltuieli
    lista = stergere_cheltuieli(13, lista)
    assert len(lista) == 4

    lista = stergere_cheltuieli(12, lista)
    assert len(lista) == 3
    assert get_id(2) is None


def test_adauga_valoare_la_cheltuieli():
    lista = lst_cheltuieli
    lista = adauga_valoare("25.06.2021", 10, lista)
    assert len(lista) == 4
    assert get_suma(lista[0]) == 160
    assert get_suma(lista[1]) == 178
    assert get_suma(lista[2]) == 312
    assert get_suma(lista[3]) == 211


def test_cea_mai_mare_cheltuiala():
    lista = lst_cheltuieli
    assert cea_mai_mare_cheltuiala("canal") == lista[1]
    assert cea_mai_mare_cheltuiala("întreținere") == lista[3]
    assert cea_mai_mare_cheltuiala(" ") is None


def test_ordonare_descrescatoare():
    lista = lst_cheltuieli
    lista = ordonare_descrescatoare(lista)
    assert len(lista) == 4
    assert get_suma(lista[0]) == 348
    assert get_suma(lista[-1]) == 145


def test_sume_lunare():
    lista = lst_cheltuieli
    lista.append(creeaza_cheltuiala(22, 145, "03.11.2021", "canal", 5))
    sume = sume_lunare(lista)
    assert len(sume) == 3
    assert len(sume['11 2021']) == 33
    assert sume["11 2021"][22] == 230


def test_functionalitati():
    test_stergere_cheltuieli()
    test_adauga_valoare_la_cheltuieli()
    test_cea_mai_mare_cheltuiala()
    test_ordonare_descrescatoare()
    test_sume_lunare()