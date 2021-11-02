from Domain.Cheltuiala import get_str, get_numar, get_suma, get_data, get_tip, creeaza_cheltuiala
from Logic.crud import create, read, update


def show_menu():
    print('1.CRUD ')
    print('2.Reducere pret')
    print('x. Exit')


def handle_add(cheltuieli):
    numar_apartament = int(input('Dati numarul apartamentului: '))
    suma = float(input('Dati suma cheltuielii'))
    data = (input('Dati data cheltuielii'))
    tip = (input('Dati tipul cheltuielii'))
    return create(cheltuieli,numar_apartament,suma,data,tip)


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
    numar_apartament = int(input('Dati noul numar al apartamentului: '))
    suma = float(input('Dati noua suma a cheltuielii'))
    data = (input('Dati noua data a cheltuielii'))
    tip = (input('Dati noul tip al cheltuielii'))
    return update(cheltuieli,creeaza_cheltuiala(numar_apartament,suma,data,tip))


def handle_crud(cheltuieli):
    while True:
        print('1.Adaugare')
        print('2.Modificare')
        print('3.Stergere')
        print('a. Afisare')
        print('d. Detalii cheltuieli')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli)
        elif optiune == '2':
            cheltuieli = handle_update(cheltuieli)
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