def show_menu():
    print('1.CRUD ')
    print('2.Reducere pret')
    print('x. Exit')


def handle_crud(cheltuieli):
    while True:
        print('1.Adaugare')
        print('2.Modificare')
        print('3.Stergere')
        print('a. Afisare')
        print('b. Revenire')


def run_ui(cheltuieli):
    while True :
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            handle_crud(cheltuieli)




    return cheltuieli