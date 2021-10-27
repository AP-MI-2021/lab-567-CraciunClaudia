def creeaza_cheltuiala(numar_apartament,suma,data,tip):
    '''
    Creeaza o cheltuiala.
    :param numar_apartament: Numarul apartamentului,trebuie sa fie unic.
    :param suma: Suma care trebuie platita
    :param data: Data la care trebuie platita
    :param tip: Tipul cheltuielii:intretinere,canal sau alte cheltuieli.
    :return:O cheltuiala
    '''

    return {'numar':numar_apartament,
            'suma':suma,
            'data':data,
            'tip':tip}

def get_numar(apartament):
    '''
    Getter pentru numarul apartamentului.
    :param apartament: apartamentul
    :return:Numarul apartamentului
    '''
    return apartament['numar']

def get_suma(apartament):
    '''
    Getter pentru suma care trebuie platita
    :param suma:suma
    :return:Suma care trebuie platita
    '''
    return apartament['suma']
def get_data(apartament):
    '''
    Getter pentru data la care trebuie platita
    :param data: Data
    :return: Data la care trebuie platita
    '''
    return apartament['data']
def get_tip(apartament):
    '''
    Getter pentru tipul de cheltuiala
    :param tip: Tipul de cheltuiala
    :return: Tipul de cheltuiala
    '''
    return apartament['tip']

def get_str(apartament):
    return f'Apartamentul cu numarul {get_numar(apartament)},suma care trebuie platita{get_suma(apartament)},la data de {get_data(apartament)},cu tipul cheltuielii: {get_tip(apartament)}'

