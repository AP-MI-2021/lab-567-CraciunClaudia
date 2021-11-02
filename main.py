from Logic.crud import create
from Tests.test_crud import test_crud
from Userinterface.console import run_ui


def main ():
    cheltuieli = []
    cheltuieli = create(cheltuieli,1,200,'11.10.2021','canalizare')
    cheltuieli = run_ui(cheltuieli)

if __name__ == '__main__':
    test_crud()
    main()