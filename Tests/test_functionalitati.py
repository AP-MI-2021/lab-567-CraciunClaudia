from Domain.Cheltuiala import creeaza_cheltuiala, get_suma
from Logic.functionalitati import stergere_cheltuieli_pentru_numar, adaugare_valori_la_cheltuieli, \
    cea_mai_mare_cheltuiala, ordonare_cheltuieli_descrescatoare


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

def test_adaugare_valori_la_cheltuieli():
    cheltuieli = get_list()
    a_cheltuieli = creeaza_cheltuiala(3,555,'04.10.2021','canalizare')
    adaugare = adaugare_valori_la_cheltuieli(cheltuieli,a_cheltuieli)
    assert a_cheltuieli not in adaugare
    assert a_cheltuieli in cheltuieli
    assert len(adaugare) == len(cheltuieli)

def test_cea_mai_mare_cheltuiala():
    lst_cheltuieli = get_list()
    assert cea_mai_mare_cheltuiala("canal", lst_cheltuieli) == lst_cheltuieli[1]
    assert cea_mai_mare_cheltuiala("întreținere", lst_cheltuieli) == lst_cheltuieli[3]
    assert cea_mai_mare_cheltuiala(" suma > tip ", lst_cheltuieli) is None

def test_ordonare_cheltuieli_descrescatoare():
    lst_cheltuieli = get_list()
    lst_cheltuieli = ordonare_cheltuieli_descrescatoare(lst_cheltuieli)
    assert len(lst_cheltuieli) == 4
    assert get_suma(lst_cheltuieli[0]) == 200
    assert get_suma(lst_cheltuieli[-1]) == 50