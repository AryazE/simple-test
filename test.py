def test_add():
    assert 1 + 2 == 3

def test_sub():
    assert 4 - 2 == 2

def test_mul():
    assert 2 * 3 == 6

def test_div():
    assert 6 / 3 == 2

def test_loop():
    l = [1, 2, 3]
    for i in l:
        l.remove(i)
    assert len(l) == 1