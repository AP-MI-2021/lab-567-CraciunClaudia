from Domain.Cheltuiala import creeaza_cheltuiala, get_id
from Logic.CRUD import create, read, update, delete


def get_data():
    return [
        creeaza_cheltuiala(205,200,'11.10.2021','alte cheltuieli',1),
        creeaza_cheltuiala(233,350,'20.10.2021','intretinere',2),
        creeaza_cheltuiala(576,444,'4.04.2021','canalizare',3),
        creeaza_cheltuiala(999,150,'21.10.2021','alte cheltuieli',4),
        creeaza_cheltuiala(520,150,'22.10.2021','intretinere',5),
   ]


def test_create():
    cheltuieli = get_data()
    params = (55,123,'22.10.2021','intretinere',44)
    c_new = creeaza_cheltuiala(*params)
    new_cheltuieli = create(cheltuieli, *params)
    assert len(new_cheltuieli) == len(cheltuieli) + 1

    # found = False
    # for cheltuiala in new_cheltuieli:
    #     if cheltuiala == c_new:
    #         found = True
    assert c_new in new_cheltuieli


def test_read():
    cheltuieli = get_data()
    some_c = cheltuieli[2]
    assert read(cheltuieli, get_id(some_c)) == some_c
    assert read(cheltuieli, None) == cheltuieli


def test_update():
    cheltuieli = get_data()
    c_updated = creeaza_cheltuiala(205,300,'14.10.2021','alte cheltuieli',1)
    updated = update(cheltuieli, c_updated)
    assert c_updated in updated
    assert c_updated not in cheltuieli
    assert len(updated) == len(cheltuieli)


def test_delete():
    cheltuieli = get_data()
    to_delete = 3
    c_deleted = read(cheltuieli, to_delete)
    deleted = delete(cheltuieli, to_delete)
    assert c_deleted not in deleted
    assert c_deleted in cheltuieli
    assert len(deleted) == len(cheltuieli) - 1


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()



