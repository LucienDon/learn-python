"""关键字参数

@see: https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments

函数可以使用 kwarg=value 形式的关键字参数来调用。
"""

import pytest


def parrot(voltage, state='a stiff', action='voom', parrot_type='Norwegian Blue'):
    """多参数函数的示例

    这个函数接受一个必选参数(voltage)和三个可选参数
    (state, action, and type).
    """

    message = 'This parrot wouldn\'t ' + action + ' '
    message += 'if you put ' + str(voltage) + ' volts through it. '
    message += 'Lovely plumage, the ' + parrot_type + '. '
    message += 'It\'s ' + state + '!'

    return message


def test_function_keyword_arguments():
    """测试使用指定关键字参数的调用函数"""

    # parrot函数接受一个必选参数 (voltage) 还有三个可选参数 (state, action,  type).
    # 这个函数可以通过以下任何一种方式被调用:

    message = (
        "This parrot wouldn't voom if you put 1000 volts through it. "
        "Lovely plumage, the Norwegian Blue. "
        "It's a stiff!"
    )
    # 1 位置参数
    assert parrot(1000) == message
    # 1 关键字参数
    assert parrot(voltage=1000) == message

    message = (
        "This parrot wouldn't VOOOOOM if you put 1000000 volts through it. "
        "Lovely plumage, the Norwegian Blue. "
        "It's a stiff!"
    )
    # 2 关键字参数
    assert parrot(voltage=1000000, action='VOOOOOM') == message
    # 2 关键字参数
    assert parrot(action='VOOOOOM', voltage=1000000) == message

    # 3 位置参数
    message = (
        "This parrot wouldn't jump if you put 1000000 volts through it. "
        "Lovely plumage, the Norwegian Blue. "
        "It's bereft of life!"
    )
    assert parrot(1000000, 'bereft of life', 'jump') == message

    # 1 位置, 1 关键字
    message = (
        "This parrot wouldn't voom if you put 1000 volts through it. "
        "Lovely plumage, the Norwegian Blue. "
        "It's pushing up the daisies!"
    )
    assert parrot(1000, state='pushing up the daisies') == message

    # 但是下面所有的调用都是无效的。

    with pytest.raises(Exception):
        # 必须参数缺失.
        # pylint: disable=no-value-for-parameter
        parrot()

    # 在关键字参数之后的非关键字参数。
    # parrot(voltage=5.0, 'dead')

    with pytest.raises(Exception):
        # pylint: disable=redundant-keyword-arg
        parrot(110, voltage=220)

    with pytest.raises(Exception):
        # 未知的关键字参数
        # pylint: disable=unexpected-keyword-arg,no-value-for-parameter
        parrot(actor='John Cleese')

    # 在函数调用中，关键字参数必须跟在位置参数之后。传递的所有关键字参数必须与函数接受的其中一个参数匹配 (例如actor不是parrot函数的有效参数),
    # 它们的顺序并不重要。这也包括非可选参数(例如parrot(voltage=1000)也是有效的)。 参数不能接收一个值超过一次。
    # 下面是一个由于这种限制而失败的示例:
    def function_with_one_argument(number):
        return number

    with pytest.raises(Exception):
        # pylint: disable=redundant-keyword-arg
        function_with_one_argument(0, number=0)

    # 当出现 **name 的最后一个正式形参时，它将接收一个字典，其中包含除与正式形参对应的关键字参数外的所有关键字参数。
    # 这可以与 *name 的形式参数结合使用，该形式参数接收一个包含形式参数列表之外的位置参数的元组。
    # (*name 必须出现在 **name 之前。)
    # 例如，如果我们这样定义一个函数:
    def test_function(first_param, *arguments, **keywords):
        """这个函数通过“arguments”元组和关键字字典接受它的参数。"""
        assert first_param == 'first param'
        assert arguments == ('second param', 'third param')
        assert keywords == {
            'fourth_param_name': 'fourth named param',
            'fifth_param_name': 'fifth named param'
        }

    test_function(
        'first param',
        'second param',
        'third param',
        fourth_param_name='fourth named param',
        fifth_param_name='fifth named param',
    )
