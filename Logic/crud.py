from Domain.Cheltuiala import creeaza_cheltuiala, get_id


def create(lst_cheltuieli,
           numar_apartament: int, suma: float , data_c , tip , id):
    '''
    Creeaza o cheltuiala
    :param lst_cheltuieli: Lista de cheltuieli
    :param numar_apartament: Numarul apartamentului
    :param suma: Suma
    :param data_c: Data cheltuielii
    :param tip: Tipul cheltuielii
    :param id: id-ul cheltuielii
    :return: O noua lista formata din lst_cheltuieli si noua cheltuiala
    '''
    if read(lst_cheltuieli, id) is not None:
        raise ValueError(f'Exista deja o prajitura cu id-ul {id}')
    cheltuiala = creeaza_cheltuiala(numar_apartament, suma, data_c , tip , id)
    #lst_cheltuieli.append(cheltuieli)
    return lst_cheltuieli + [cheltuiala]

def read(lst_cheltuieli, id: int = None):
   '''
   Citeste o cheltuiala din baza de date

   :param lst_cheltuieli:Lista de cheltuieli
   :param id:Id-ul cheltuielii
   :return:
        - cheltuiala cu id-ul id, daca exista
        - lista cu toate cheltuielile, daca id=None
        - None, daca nu exista o cheltuiala cu id
   '''
   if not id:
       return lst_cheltuieli
   cheltuiala_cu_id = None
   for cheltuiala in lst_cheltuieli:
       if get_id(cheltuiala) == id:
           cheltuiala_cu_id = cheltuiala

   if cheltuiala_cu_id:
       return cheltuiala_cu_id
   return None





def update(lst_cheltuieli, new_cheltuiala):
    '''
    Actualizeaza o cheltuiala

    :param lst_cheltuieli:Lista cheltuielii
    :param new_cheltuiala:cheltuiala care se va actualiza - numarul trebuie sa fie unul existent
    :return:O lista cu cheltuiala actualizata
    '''

    # lst_cheltuieli=[p1:(1,205), p2:(2,301)], cheltuiala=(2,402)
    if read(lst_cheltuieli, get_id(new_cheltuiala)) is None:
        raise ValueError(f'Nu xista o cheltuiala cu id-ul {get_id(new_cheltuiala)} pe care sa o actualizam.')
    new_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != get_id(new_cheltuiala):
            new_cheltuieli.append(cheltuiala)
        else:
            new_cheltuieli.append(new_cheltuiala)
    return new_cheltuieli

def delete(lst_cheltuieli, id: int):
    '''
    Sterge o cheltuiala din baza de date

    :param lst_cheltuieli:lista de cheltuieli
    :param id:id-ul cheltuielii
    :return:O lista de cheltuieli fara cheltuiala cu id-ul de cheltuiala id
    '''
    if read(lst_cheltuieli, id) is None:
        raise ValueError(f'Nu xista o cheltuiala cu id-ul {id} pe care sa o stergem.')
    new_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != id:
            new_cheltuieli.append(cheltuiala)

    return new_cheltuieli

