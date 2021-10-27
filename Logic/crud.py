from Domain.Cheltuiala import creeaza_cheltuiala, get_numar


def create(lst_cheltuieli, numar_apartament:int , suma, data, tip, creeaza_cheltuieli):
    '''

    :param lst_cheltuieli: Lista de cheltuieli
    :param numar_apartament: Numarul apartamentului
    :param suma:suma
    :param data:data cheltuielii
    :param tip:tipul cheltuielii: intretinere,canal,altele
    :return:O noua lista formata din lst_cheltuieli si noua cheltuiala
    '''
    cheltuiala = creeaza_cheltuiala(numar_apartament,suma,data,tip)
    #lst_cheltuieli.append(cheltuiala)
    return lst_cheltuieli + [cheltuiala]

def read(lst_cheltuieli,numar_apartament=None):
    '''
    Citeste o prajitura din baza de date
    :param lst_cheltuieli:lista de cheltuieli
    :param numar_apartament: Numarul apartamentului
    :return:Apartamentul cu numarul numar_apartament sau lista cu toate cheltuielile daca numar_apartament=None
    '''
    apartament_cu_numar=None

    for cheltuiala in lst_cheltuieli:
        if get_numar(numar_apartament) == numar_apartament:
            apartament_cu_numar = numar_apartament

    if apartament_cu_numar:
        return apartament_cu_numar
    return lst_cheltuieli

def update(lst_cheltuieli,new_cheltuiala):
    '''
    Actualizeaza o cheltuiala.
    :param lst_cheltuieli:Lista de cheltuieli
    :param new_cheltuiala:cheltuiala care se va actualiza - numarul trebuie sa fie unul existent
    :return:O lista cu cheltuiala actualizata
    '''
    #lst_cheltuieli= [c1:(1,2008),p2:(2,2009)], cheltuiala=(2,2038)
    new_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_numar(cheltuiala) != get_numar(new_cheltuiala):
            new_cheltuieli.append(cheltuiala)
        else:
            new_cheltuieli.append(new_cheltuiala)
    return new_cheltuieli

def delete(lst_cheltuieli,numar_apartament):
    '''

    :param lst_cheltuieli:
    :param numar_apartament:
    :return:O lista de cheltuieli fara cheltuiala cu numarul de apartament numar_apartament
    '''
    new_cheltuieli= []
    for cheltuiala in lst_cheltuieli :
        if get_numar(numar_apartament) != numar_apartament :
            new_cheltuieli.append(numar_apartament)
    return new_cheltuieli