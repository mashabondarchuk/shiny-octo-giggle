from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 2) == 4

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(8, 2) == 4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(8, 0)
