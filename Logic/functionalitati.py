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



