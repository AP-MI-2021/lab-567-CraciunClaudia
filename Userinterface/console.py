from Domain.Cheltuiala import get_str, get_numar, get_suma, get_data_c, get_tip, creeaza_cheltuiala
from Logic.crud import create, read, update, delete
from Logic.functionalitati import stergere_cheltuieli, adauga_valoare, cea_mai_mare_cheltuiala, ordonare_descrescatoare, \
    sume_lunare


def show_menu():
    print('1. CRUD')
    print('2. Stergerea tuturor cheltuielilor .')
    print('x. Exit')


def handle_add(cheltuieli):
    numar_apartament = int(input('Dati numarul apartamentului: '))
    suma = float(input('Dati suma cheltuielii: '))
    data_c = (input('Dati data cheltuielii: '))
    tip = int(input('Dati tipul cheltuielii: '))
    id = int(input('Dati id-ul cheltuielii: '))
    return create(cheltuieli,numar_apartament, suma , data_c , tip , id)


def handle_show_all(cheltuieli):
    for cheltuiala in cheltuieli:
        print(get_str(cheltuiala))


def handle_show_details(cheltuieli):
    id = int(input('Dati id-ul cheltuielii pentru care doriti detalii: '))
    cheltuiala = read(cheltuieli, id)
    print(f'Numar: {get_numar(cheltuiala)}')
    print(f'Suma: {get_suma(cheltuiala)}')
    print(f'Data: {get_data_c(cheltuiala)}')
    print(f'Tip: {get_tip(cheltuiala)}')



def handle_update(cheltuieli):
    id = int(input('Dati id-ul cheltuielii care se actualizeaza: '))
    numar_apartament = int(input('Dati noul numar al cheltuielii: '))
    suma = float(input('Dati noua suma a cheltuielii: '))
    data_c = float(input('Dati noua data a cheltuielii: '))
    tip = int(input('Dati noul tip al cheltuielii: '))
    return update(cheltuieli, creeaza_cheltuiala(numar_apartament, suma , data_c , tip , id))


def handle_delete(cheltuieli):
    id = int(input('Dati id-ul cheltuielii care se va sterge: '))
    cheltuieli = delete(cheltuieli, id)
    print('Stergerea a fost efectuata cu succes.')
    return cheltuieli


def handle_delete_all(cheltuieli):
    id = int(input('Dati id-ul cheltuielii pentru care se vor sterge cheltuielile unui apartament dat: '))
    cheltuieli = stergere_cheltuieli(cheltuieli,id)
    print('Stergerea a fost efectuata cu succes')
    return cheltuieli


def handle_adauga_valoare(cheltuieli):
    id = int(input('Dati id-ul pentru care se va adauga valoarea: '))
    data_c = input('Dati data pentru care se va adauga valoarea: ')
    valoare = input('Dati valoarea care se va adauga: ')
    cheltuieli = adauga_valoare(cheltuieli,data_c,valoare)
    return cheltuieli


def handle_cea_mai_mare_cheltuiala(cheltuieli):
    new = cea_mai_mare_cheltuiala(cheltuieli)
    for tip in new:
        print(f'Pentru tipul: {tip} avem cheltuiala: {get_str(new[tip])}')


def handle_ordonare_descrescatoare(cheltuieli):
    lst_cheltuieli = ordonare_descrescatoare(cheltuieli)
    print ('Cheltuielile au fost ordonate descrescator')
    return lst_cheltuieli


def handle_sume_lunare(cheltuieli):
    new = sume_lunare(cheltuieli)
    for luna in new:
        print(f'Pentru Luna {luna} avem lista de sume: {new[luna]}')


def handle_crud(cheltuieli):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('4. Stergere cheltuieli')
        print('5. Adauga valoare')
        print('6. Cea mai mare cheltuiala')
        print('7 . Ordonare descrescatoare')
        print('8. Sume lunare')
        print('a. Afisare')
        print('d. Detalii cheltuiala')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli)
        elif optiune == '2':
            cheltuieli = handle_update(cheltuieli)
        elif optiune == '3':
            cheltuieli = handle_delete(cheltuieli)
        elif optiune == '4':
            cheltuieli = handle_delete_all(cheltuieli)
        elif optiune == '5':
            cheltuieli = handle_adauga_valoare(cheltuieli)
        elif optiune == '6':
            handle_cea_mai_mare_cheltuiala(cheltuieli)
        elif optiune == '7':
            cheltuieli = handle_ordonare_descrescatoare(cheltuieli)
        elif optiune == '8':
            handle_sume_lunare(cheltuieli)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'd':
            handle_show_details(cheltuieli)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return cheltuieli


def run_ui(cheltuieli):

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_crud(cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return cheltuieli