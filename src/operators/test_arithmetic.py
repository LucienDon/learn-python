"""算术运算符

@see: https://www.w3schools.com/python/python_operators.asp

算术运算符用于数值来执行常见的数学运算
"""


def test_arithmetic_operators():
    """算术运算符"""

    # 加.
    assert 5 + 3 == 8

    # 减.
    assert 5 - 3 == 2

    # 乘.
    assert 5 * 3 == 15
    assert isinstance(5 * 3, int)

    # 除.
    # 除法的结果是浮点数.
    assert 5 / 3 == 1.6666666666666667
    assert 8 / 4 == 2
    assert isinstance(5 / 3, float)
    assert isinstance(8 / 4, float)

    # 模运算.
    assert 5 % 3 == 2

    #  取幂.
    assert 5 ** 3 == 125
    assert 2 ** 3 == 8
    assert 2 ** 4 == 16
    assert 2 ** 5 == 32
    assert isinstance(5 ** 3, int)

    # 向下取整除数.
    assert 5 // 3 == 1
    assert 6 // 3 == 2
    assert 7 // 3 == 2
    assert 9 // 3 == 3
    assert isinstance(5 // 3, int)
