from pytestdemo.calc import add, divide, multiply, sub


def test_add():
    """test add"""
    assert add(6, 3) == 9


def test_sub():
    """test sub"""
    assert sub(6, 3) == 3


def test_multiply():
    """test multiply"""
    assert multiply(6, 3) == 18


def test_divide_ok():
    """test divide ok"""
    assert divide(6, 3) == 2


# 「カバレッジ = 100％」にしない場合の確認のためコメントアウト
# def test_divide_zero_division_error():
#    with pytest.raises(ZeroDivisionError):
#        assert divide(6, 0)
