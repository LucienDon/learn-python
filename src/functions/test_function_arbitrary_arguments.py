"""任意的参数列表

@see: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists

函数可以使用任意数量的参数来调用。这些参数将封装在一个元组中。
在可变数量的参数之前，可能会出现零个或多个普通参数。
"""


def test_function_arbitrary_arguments():
    """任意的参数列表"""

    # 当出现 **name 的最后一个正式形参时，它将接收一个字典，其中包含除与正式形参对应的关键字参数外的所有关键字参数。
    # 这可以与 *name 的形式参数结合使用，该形式参数接收一个包含形式参数列表之外的位置参数的元组。
    # (*name 必须出现在 **name之前。)例如，如果我们这样定义一个函数:
    def test_function(first_param, *arguments):
        """这个函数通过“arguments”元组和关键字字典接受它的参数。"""
        assert first_param == 'first param'
        assert arguments == ('second param', 'third param')

    test_function('first param', 'second param', 'third param')

    # 通常，这些可变参数将位于形参列表的最后，因为它们将获取传递给函数的所有剩余输入参数。
    # 任何出现在*args形参之后的形式形参都是“仅关键字”参数，这意味着它们只能作为关键字而不是位置参数使用。
    def concat(*args, sep='/'):
        return sep.join(args)

    assert concat('earth', 'mars', 'venus') == 'earth/mars/venus'
    assert concat('earth', 'mars', 'venus', sep='.') == 'earth.mars.venus'
