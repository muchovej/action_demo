from src.add import add

def test_addition_happy_path():
    assert add(4, 2) == 6

def test_addition_negative_values():
    assert add(-3, -2) == -5

def test_add_one_neg_value():
    assert add(-3, 2) == -1
