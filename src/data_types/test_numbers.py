"""数字.

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_numbers.asp

Python中有三种数值类型:
- int (e.g. 2, 4, 20)
    - bool (e.g. False and True, acting like 0 and 1)
- float (e.g. 5.0, 1.6)
- complex (e.g. 5+6j, 4-3j)
"""


def test_integer_numbers():
    """Integer type

    Int或integer是一个整数，无论正或负，没有小数，无限长.
    """

    positive_integer = 1
    negative_integer = -3255522
    big_integer = 35656222554887711

    assert isinstance(positive_integer, int)
    assert isinstance(negative_integer, int)
    assert isinstance(big_integer, int)


def test_booleans():
    """Boolean

   布尔值表示真值False和True。表示值的两个对象False和True是唯一的布尔对象。
   布尔类型是整数类型的子类型，和布尔值的行为类似于值0和1，在几乎所有上下文中
   例外是当转换为字符串时，返回字符串"False"或"True"
    """

    true_boolean = True
    false_boolean = False

    assert true_boolean
    assert not false_boolean

    assert isinstance(true_boolean, bool)
    assert isinstance(false_boolean, bool)

    # 让我们尝试将布尔类型转换为字符串。
    assert str(true_boolean) == "True"
    assert str(false_boolean) == "False"


def test_float_numbers():
    """Float type

    浮点数，或“浮点数”是一个数，无论正或负，包含一个或多个小数的
    """

    float_number = 7.0
    # 另一种声明浮点数的方法是使用float()函数。
    float_number_via_function = float(7)
    float_negative = -35.59

    assert float_number == float_number_via_function
    assert isinstance(float_number, float)
    assert isinstance(float_number_via_function, float)
    assert isinstance(float_negative, float)

    # Float也可以是用“e”表示的科学数字 10 的幂。
    float_with_small_e = 35e3
    float_with_big_e = 12E4

    assert float_with_small_e == 35000
    assert float_with_big_e == 120000
    assert isinstance(12E4, float)
    assert isinstance(-87.7e100, float)


def test_complex_numbers():
    """复数型"""

    complex_number_1 = 5 + 6j
    complex_number_2 = 3 - 2j

    assert isinstance(complex_number_1, complex)
    assert isinstance(complex_number_2, complex)
    assert complex_number_1 * complex_number_2 == 27 + 8j


def test_number_operators():
    """ 基本运算"""

    #  加法.
    assert 2 + 4 == 6

    #  乘法.
    assert 2 * 4 == 8

    # 除法总是返回浮点数.
    assert 12 / 3 == 4.0
    assert 12 / 5 == 2.4
    assert 17 / 3 == 5.666666666666667

    # 取模运算符返回除法的余数.
    assert 12 % 3 == 0
    assert 13 % 3 == 1

    # 除法向下取整摒弃了小数部分.
    assert 17 // 3 == 5

    # 把数字提高到特定的幂。
    assert 5 ** 2 == 25  # 5的平方
    assert 2 ** 7 == 128  # 2的7次方

    # 运算符与混合类型操作数将整数操作数转换为浮点数。
    assert 4 * 3.75 - 1 == 14.0
