def creeaza_cheltuiala(numar_apartament: int, suma: float , data_c , tip , id):
    '''
    Creeaza o cheltuiala.
    :param numar_apartament: Numarul apartamentului
    :param suma: Suma
    :param data_c: Data cheltuielii
    :param tip: Tipul cheltuielii (canalizare,intretinere,alte cheltuieli)
    :param id:id-ul cheltuielii.Trebuie sa fie unic.
    :return:O cheltuiala
    '''
    return {
        'numar' : numar_apartament,
        'suma' : suma,
        'data_c' : data_c,
        'tip' :tip,
        'id' : id

    }

def get_numar(cheltuiala):
    '''
    Getter pentru numarul apartamentului
    :param cheltuiala:cheltuiala
    :return:numarul apartamentului
    '''
    return cheltuiala['numar']

def get_suma(cheltuiala):
    '''
    Getter pentru suma
    :param cheltuiala:Cheltuiala
    :return:Suma cheltuielii
    '''
    return cheltuiala['suma']

def get_data_c(cheltuiala):
    '''
    Getter pentru data cheltuielii
    :param cheltuiala: Cheltuiala
    :return: Data cheltuielii
    '''
    return cheltuiala['data_c']

def get_tip(cheltuiala):
    '''
    Getter pentru tipul cheltuielii
    :param cheltuiala: Cheltuiala
    :return: Tipul cheltuielii
    '''
    return cheltuiala['tip']

def get_id(cheltuiala):
    '''
    Getter pentru id-ul cheltuielii
    :param cheltuiala: Cheltuiala
    :return: Id-ul cheltuielii
    '''
    return cheltuiala['id']

def get_str(cheltuiala):
    return f'Cheltuiala cu id-ul {get_id(cheltuiala)}, cu numarul {get_numar(cheltuiala)}, cu suma {get_suma(cheltuiala)},din data {get_data_c(cheltuiala)}, cu tipul {get_tip(cheltuiala)} '