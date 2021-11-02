from Domain.Cheltuiala import creeaza_cheltuiala
from Logic.functionalitati import stergere_cheltuieli_pentru_numar


def get_list():
    return [
        creeaza_cheltuiala (200,556,'13.09.2020','canalizare'),
        creeaza_cheltuiala(5,400,'11.12.2021','intretinere'),
        creeaza_cheltuiala(2,45,'11.11.2021','alte cheltuieli'),
    ]

def test_sterge_cheltuieli():
    cheltuieli = get_list()
    s_cheltuieli = creeaza_cheltuiala(2,5050,'03.09.2020','alte cheltuieli')
    stergere = stergere_cheltuieli_pentru_numar(cheltuieli,s_cheltuieli)
    assert s_cheltuieli not in stergere
    assert s_cheltuieli in cheltuieli
    assert len(stergere) == len(cheltuieli)

