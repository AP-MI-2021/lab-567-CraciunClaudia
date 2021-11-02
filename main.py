from Logic.crud import create
from Tests.test_crud import test_crud
from Userinterface.console import run_ui


def main ():
    cheltuieli = []
    cheltuieli = create(cheltuieli,1,200,'11.10.2021','canalizare',50)
    cheltuieli = create(cheltuieli,2,50,'09.08.2020','intretinere',20)
    cheltuieli = create(cheltuieli,3,500,'01.01.2021','alte cheltuieli',40)
    cheltuieli = run_ui(cheltuieli)

if __name__ == '__main__':
    test_crud()
    main()