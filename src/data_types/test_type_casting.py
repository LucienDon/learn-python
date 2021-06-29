"""类型转换

@see: https://www.w3schools.com/python/python_casting.asp

有时您可能希望为变量指定类型。这可以通过转换来实现。
Python是一种面向对象的语言，因此它使用类来定义数据类型， 包括它的基本类型。

因此 python 中的类型转换是使用构造函数来完成的:

- int() - 从一个整数字面值、一个浮点字面值(通过四舍五入)构造一个整数到前一个整数)字面值，或字符串字面值(提供字符串表示整数)

- float() - 从整数字面值、浮点字面值或字符串字面值(提供表示浮点数或整数的字符串)构造浮点数

- str() - 从各种数据类型构造字符串，包括字符串、整型字面值和浮点字面值
"""


def test_type_casting_to_integer():
    """类型转换为整数"""

    assert int(1) == 1
    assert int(2.8) == 2
    assert int('3') == 3


def test_type_casting_to_float():
    """类型转换为浮点数"""

    assert float(1) == 1.0
    assert float(2.8) == 2.8
    assert float("3") == 3.0
    assert float("4.2") == 4.2


def test_type_casting_to_string():
    """类型转换为字符串"""

    assert str("s1") == 's1'
    assert str(2) == '2'
    assert str(3.0) == '3.0'
