"""默认参数值

@see: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values

最有用的形式是为一个或多个参数指定默认值。这样就创建了一个函数，调用它的参数比定义允许的参数要少。
"""


def power_of(number, power=2):
    """ 将数字提高到特定的幂。

    您可能会注意到，默认情况下，该函数引发number的2次方。
    """
    return number ** power


def test_default_function_arguments():
    """测试默认函数参数"""

    # power_of 函数可以通过多种方式调用，因为第二个参数有默认值。首先，我们可以称它完全省略了第二个参数。
    assert power_of(3) == 9
    # 还可以使用以下函数调用重写第二个参数。
    assert power_of(3, 2) == 9
    assert power_of(3, 3) == 27
