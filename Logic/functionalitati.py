from Domain.Cheltuiala import get_numar, get_data, get_suma, get_tip
from Logic.crud import create


def stergere_cheltuieli_pentru_numar(lst_cheltuieli,numar_apartament):
    '''
    Sterge toate cheltuielile dintr-un apartament.
    :param lst_cheltuieli: Lista de cheltuieli
    :param numar_apartament: numar
    :return:lista in care cheltuielile s-au sters
    '''
    for cheltuiala in lst_cheltuieli:
        if get_numar(cheltuiala) == numar_apartament:
            lst_cheltuieli = stergere_cheltuieli_pentru_numar(lst_cheltuieli,numar_apartament)
    return lst_cheltuieli

def adaugare_valori_la_cheltuieli(data,suma,lst_cheltuieli):
    '''
    Adauga o valoare la toate cheltuielile dintr-o anumita data.
    :param data:Data la care se adauga cheltuielile
    :param suma:Suma adaugata la cheltuieli
    :param lst_cheltuieli:
    :return:Lista cu valoarea adaugata la toate cheltuielile dintr-o anumita data.
    '''
    data = get_data(data)

    for cheltuiala in lst_cheltuieli:
        if get_data(cheltuiala) == data:
            lst_cheltuieli = create(
                get_numar(cheltuiala),
                get_suma(cheltuiala) + suma,
                get_data(cheltuiala),
                get_tip(cheltuiala),
                lst_cheltuieli,
            )
    return lst_cheltuieli

def cea_mai_mare_cheltuiala(tip,lst_cheltuieli):
    '''
    Determina cea mai mare cheltuiala dintr-o lista
    :param tip: Tipul cheltuielii
    :param lst_cheltuieli: lista de cheltuieli
    :return: Cea mai mare cheltuiala din lista
    '''
    cheltuiala_max = None

    for cheltuiala in lst_cheltuieli:
        if get_tip(cheltuiala) == tip and (
                cheltuiala_max is None or get_suma(cheltuiala) > get_suma(cheltuiala_max) ):
            cheltuiala_max = cheltuiala

    return cheltuiala_max

def ordonare_cheltuieli_descrescatoare(lst_cheltuieli):
    lst_cheltuieli.sort(reverse=True, key=lambda cheltuiala: get_suma(cheltuiala))
    return lst_cheltuieli

