from Domain.Cheltuiala import get_numar


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



