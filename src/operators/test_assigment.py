"""赋值运算符

@see: https://www.w3schools.com/python/python_operators.asp

赋值运算符用于给变量赋值
"""


def test_assignment_operator():
    """ 赋值运算符 """

    # 赋值: =
    number = 5
    assert number == 5

    #  多重赋值.
    # 变量first_variable和second_variable同时得到新的值0和1。
    first_variable, second_variable = 0, 1
    assert first_variable == 0
    assert second_variable == 1

    # 您甚至可以使用多次赋值来切换变量值。
    first_variable, second_variable = second_variable, first_variable
    assert first_variable == 1
    assert second_variable == 0


def test_augmented_assignment_operators():
    """赋值操作符结合算术操作符和位操作符"""

    # 赋值: +=
    number = 5
    number += 3
    assert number == 8

    # 赋值: -=
    number = 5
    number -= 3
    assert number == 2

    # 赋值: *=
    number = 5
    number *= 3
    assert number == 15

    # 赋值: /=
    number = 8
    number /= 4
    assert number == 2

    # 赋值: %=
    number = 8
    number %= 3
    assert number == 2

    # 赋值: %=
    number = 5
    number %= 3
    assert number == 2

    # 赋值: //=
    number = 5
    number //= 3
    assert number == 1

    # 赋值: **=
    number = 5
    number **= 3
    assert number == 125

    # 赋值: &=
    number = 5  # 0b0101
    number &= 3  # 0b0011
    assert number == 1  # 0b0001

    # 赋值: |=
    number = 5  # 0b0101
    number |= 3  # 0b0011
    assert number == 7  # 0b0111

    # 赋值: ^=
    number = 5  # 0b0101
    number ^= 3  # 0b0011
    assert number == 6  # 0b0110

    # 赋值: >>=
    number = 5
    number >>= 3
    assert number == 0  # (((5 // 2) // 2) // 2)

    # 赋值: <<=
    number = 5
    number <<= 3
    assert number == 40  # 5 * 2 * 2 * 2
