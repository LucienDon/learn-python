"""拆包参数列表

@see: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists

解包参数可以通过和操作符执行。详情见下文。
"""


def test_function_unpacking_arguments():
    """拆包参数列表"""

    # 当参数已经在列表或元组中，但需要为需要单独位置参数的函数调用解包时，可能会出现这种情况。
    # 例如，内置的range()函数需要单独的start和stop参数。如果它们不能单独使用，
    # 则使用 *-operator 编写函数调用，将参数从列表或元组中解包:

    # 带有不同参数的普通调用:
    assert list(range(3, 6)) == [3, 4, 5]

    # 使用从列表中解包的参数调用。
    arguments_list = [3, 6]
    assert list(range(*arguments_list)) == [3, 4, 5]

    # 以同样的方式，字典可以使用 **-operator:
    def function_that_receives_names_arguments(first_word, second_word):
        return first_word + ', ' + second_word + '!'

    arguments_dictionary = {'first_word': 'Hello', 'second_word': 'World'}
    assert function_that_receives_names_arguments(**arguments_dictionary) == 'Hello, World!'
