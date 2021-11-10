from Logic.crud import create
from Tests.test_crud import test_crud
from Userinterface.console import run_ui


def main():
    cheltuieli = []
    cheltuieli = create(cheltuieli,505,200,'11.10.2021','alte cheltuieli',1)
    cheltuieli = create(cheltuieli,221,445.55,'12.11.2021','canalizare',55)
    cheltuieli = create(cheltuieli,333,511.42,'20.11.2021','intretinere',42)
    cheltuieli = run_ui(cheltuieli)

if __name__ == '__main__':
    test_crud()
    main()