from Domain.Cheltuiala import creeaza_cheltuiala, get_numar
from Logic.crud import create, read, update, delete


def get_data():
    return [
        creeaza_cheltuiala(1,100,'20.11.2021','canalizare'),
        creeaza_cheltuiala(2,200,'10.11.2021','intretinere'),
        creeaza_cheltuiala(3,250,'21.11.2021','alte cheltuieli')]

def test_create():
    cheltuieli= get_data()
    params = (100,2050,'10.11.2021','alte cheltuieli')
    c_new = creeaza_cheltuiala(*params)
    new_cheltuieli = create(cheltuieli , *params)
    assert len(new_cheltuieli) == len(cheltuieli) + 1

    params2 = (50,20,'1.1.1','hgfd')
    try:
        _ = create(new_cheltuieli,*params2)
        assert False
    except ValueError:
        assert True # sau pass



    #found = False
    #for cheltuiala in new_cheltuieli:
    #    if cheltuiala == c_new :
    #        found = True
    assert c_new in new_cheltuieli

def test_read():
    cheltuieli = get_data()
    some_c = cheltuieli [2]
    assert read(cheltuieli,get_numar(some_c) == some_c)
    assert read(cheltuieli,None) == cheltuieli

def test_update():
    cheltuieli = get_data()
    c_updated = creeaza_cheltuiala(1,2010,'11.10.2021','canalizare')
    updated = update(cheltuieli,c_updated)
    assert c_updated in updated
    assert c_updated not in cheltuieli
    assert len(updated) == len(cheltuieli)

def test_delete():
    cheltuieli = get_data()
    to_delete = 3
    c_deleted = read(cheltuieli,to_delete)
    deleted = delete(cheltuieli,to_delete)
    assert c_deleted not in deleted
    assert c_deleted in cheltuieli
    assert len(deleted) == len(cheltuieli) -1

def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()



