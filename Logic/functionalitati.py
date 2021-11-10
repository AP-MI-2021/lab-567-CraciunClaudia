from Domain.Cheltuiala import get_numar, get_id, get_data_c, get_suma, get_tip, creeaza_cheltuiala
from Logic.CRUD import delete


def stergere_cheltuieli(numar_apartament, lst_cheltuieli):
    '''
    Sterge toate cheltuielile unui apartament din lista.
    :param numar_apartament: Numarul apartamentului
    :param lst_cheltuieli: Lista de cheltuieli
    :return: O lista fara cheltuielile unui apartament din lista
    '''
    for cheltuiala in lst_cheltuieli:
        if get_numar(cheltuiala) == numar_apartament:
           lst_cheltuieli = delete(get_id(cheltuiala),lst_cheltuieli)
    return lst_cheltuieli

def adauga_valoare(lst_cheltuieli,data_c,valoare):
    '''
    Adauga o valoare la toate cheltuielile dintr-o anumita data.
    :param lst_cheltuieli: Lista de cheltuieli
    :param data_c: Data cheltuielii
    :param valoare: Valoarea care se adauga la cheltuiala dintr-o anumita data
    :return: Lista cu valoarea adaugata la toate cheltuielile dintr-o anumita data
    '''

    verificare = False

    new_list = []
    for cheltuiala in lst_cheltuieli:
        if get_data_c(cheltuiala) == data_c:
            verificare = True
            suma_noua = get_suma(cheltuiala) + valoare
            id = get_id(cheltuiala)
            nr_ap = get_numar(cheltuiala)
            tip = get_tip(cheltuiala)
            new_list.append(creeaza_cheltuiala(id, nr_ap, suma_noua, data_c, tip))
        else:
            new_list.append(cheltuiala)
    if verificare == False:
        raise ValueError('Nu exista data citita')
    return new_list


def cea_mai_mare_cheltuiala(lst_cheltuieli):
    '''
    Determina cea mai mare cheltuiala .
    :param lst_cheltuieli: Lista de cheltuieli
    :return: Cea mai mare cheltuiala din lista
    '''

    new = {}
    for cheltuiala in lst_cheltuieli:
        tip = get_tip(cheltuiala)
        suma = get_suma(cheltuiala)
        if tip in new:
            if suma > get_suma(new[tip]):
                new[tip] = cheltuiala
        else:
            new[tip] = cheltuiala
    return new


def ordonare_descrescatoare(lst_cheltuieli):
    '''
    Ordoneaza cheltuielile in ordine descrescatoare in functie de suma.
    :param lst_cheltuieli: Lista de cheltuieli
    :return: Cheltuielile in ordine descrescatoare
    '''
    lst_cheltuieli.sort(reverse=True, key=lambda cheltuiala: get_suma(cheltuiala))
    return lst_cheltuieli

def sume_lunare(lista):
    '''
    Returneaza un dictionar cu sumele lunare pentru fiecare apartament.
    :param lista: Lista de cheltuieli
    :return: Sumele lunare pentru fiecare apartament
    '''
    sume = {}
    for cheltuiala in lista:
        luna = get_data_c(cheltuiala).strftime("%m %Y")
        apartament = get_numar(cheltuiala)

        if luna not in sume:
            sume[luna] = {}

        if apartament in sume[luna]:
            sume[luna][apartament] += get_suma(cheltuiala)
        else:
            sume[luna][apartament] = get_suma(cheltuiala)

    return sume
