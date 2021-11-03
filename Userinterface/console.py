from Domain.Cheltuiala import get_str, get_numar, get_suma, get_data, get_tip, creeaza_cheltuiala
from Logic.crud import create, read, update, delete
from Logic.functionalitati import stergere_cheltuieli_pentru_numar, adaugare_valori_la_cheltuieli, \
    cea_mai_mare_cheltuiala


def show_menu():
    print('1.CRUD ')
    print('2.Stergere toate cheltuieli')
    print('x. Exit')


def handle_add(cheltuieli):
    try:
        numar_apartament = int(input('Dati numarul apartamentului: '))
        suma = float(input('Dati suma cheltuielii'))
        data = (input('Dati data cheltuielii'))
        tip = (input('Dati tipul cheltuielii'))

        return create(cheltuieli,numar_apartament,suma,data,tip)
    except ValueError as ve:
        print('Eroare: ',ve)
    return cheltuieli

def handle_show_all(cheltuieli):
    for cheltuiala in cheltuieli :
        print(get_str(cheltuiala))





def handle_show_details(cheltuieli):
    numar_apartament = int(input('Dati numarul apartamentului pentru care doriti detalii: '))
    cheltuiala = read(cheltuieli,numar_apartament)
    print(f'Numar: {get_numar(cheltuiala)}')
    print(f'Suma: {get_suma(cheltuiala)}')
    print(f'Data: {get_data(cheltuiala)}')
    print(f'Tip: {get_tip(cheltuiala)}')


def handle_update(cheltuieli):
    try:
        numar_apartament = int(input('Dati noul numar al apartamentului: '))
        suma = float(input('Dati noua suma a cheltuielii: '))
        data = (input('Dati noua data a cheltuielii: '))
        tip = (input('Dati noul tip al cheltuielii: '))
        return update(cheltuieli,creeaza_cheltuiala(numar_apartament,suma,data,tip))
    except ValueError as ve:
        print('Eroare:',ve)
    return cheltuieli



def handle_delete(cheltuieli):
    try:
        numar_apartament = int(input('Dati numarul apartamentului care se va sterge: '))
        cheltuieli = delete(cheltuieli,numar_apartament)
        print ('Stergerea a fost efectuata cu succes!')
        return cheltuieli
    except ValueError as ve:
        print('Eroare:',ve)
    return cheltuieli


def handle_stergere_cheltuieli(cheltuieli):
    numar = input('Dati numarul cautat pentru stergerea cheltuielilor: ')
    cheltuieli = stergere_cheltuieli_pentru_numar(cheltuieli,numar)
    print('Toate cheltuielile au fost sterse.')
    return cheltuieli


def handle_adaugare_cheltuieli(lst_cheltuieli):
    id = input('Introduceti id: ')
    try:
        numar_apartament = int(input("Introduceti numarul apartamentului: "))
        suma = float(input("Introduceti suma: "))
        data = input("Intrdouceti data: ")
        tip = input("Introduceti tipul cheltuielii: ")
        lst_cheltuieli = adaugare_valori_la_cheltuieli(
            creeaza_cheltuiala(numar_apartament, suma, data, tip,id),lst_cheltuieli)
    except ValueError as ve:
        print('Eroare:',ve)

    return lst_cheltuieli


def handle_adaugare_valori_cheltuieli(lst_cheltuieli):
    try:
        data = input("Introduceti data: ")
        suma = float(input("Introduceti suma: "))
        lst_cheltuieli = adaugare_valori_la_cheltuieli(data, suma, lst_cheltuieli)
    except ValueError as ve:
        print('Eroare:',ve)
    return lst_cheltuieli


def handle_cea_mai_mare_cheltuiala(lst_cheltuieli):
    cheltuieli = cea_mai_mare_cheltuiala(lst_cheltuieli)
    for tip in cheltuieli:
        print('Tipul {} are suma maxima {}'.format(tip, cheltuieli[tip]))


def handle_crud(cheltuieli):
    while True:
        print('1.Adaugare')
        print('2.Modificare')
        print('3.Stergere')
        print('4.Stergere cheltuieli')
        print('5.Adaugare suma la cheltuiala')
        print('6.Adaugare valori la cheltuieli')
        print('7.Cea mai mare cheltuiala')
        print('a. Afisare')
        print('d. Detalii cheltuieli')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli)
        elif optiune == '2':
            cheltuieli = handle_update(cheltuieli)
        elif optiune == '3':
            cheltuieli = handle_delete(cheltuieli)
        elif optiune == '4':
            cheltuieli= handle_stergere_cheltuieli(cheltuieli)
        elif optiune == '5':
            cheltuieli=handle_adaugare_cheltuieli(cheltuieli)
        elif optiune == '6':
            cheltuieli = handle_adaugare_valori_cheltuieli(cheltuieli)
        elif optiune == '7':
            cheltuieli = handle_cea_mai_mare_cheltuiala(cheltuieli)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'd':
            handle_show_details(cheltuieli)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')

    return cheltuieli


def run_ui(cheltuieli):
    while True :
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_crud(cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')




    return cheltuieli