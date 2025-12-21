from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 10) == 0
    assert subtract(5, -5) == 10
    assert subtract(-5, 5) == -10


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0


def test_divide():
    assert divide(6, 3) == 2
    assert divide(10, 1) == 10


def test_divide_by_zero():
    assert divide(5, 0) is None
    assert divide(0, 0) is None
