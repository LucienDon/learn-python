"""Lambda 表达式

@see: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

可以使用lambda关键字创建小型匿名函数。
Lambda函数可以在任何需要函数对象的地方使用。
它们在语法上仅限于单个表达式。从语义上讲，它们只是普通函数定义的语法糖。
与嵌套函数定义一样，lambda函数可以引用包含范围内的变量。
"""


def test_lambda_expressions():
    """Lambda  表达式"""

    # 这个函数返回两个参数的和:lambda a, b: a+b
    # 与嵌套函数定义一样，lambda函数可以引用包含范围内的变量。

    def make_increment_function(delta):
        """本例使用 lambda 表达式返回函数"""
        return lambda number: number + delta

    increment_function = make_increment_function(42)

    assert increment_function(0) == 42
    assert increment_function(1) == 43
    assert increment_function(2) == 44

    # lambda 的另一种用法是将一个小函数作为参数传递。
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    # 按文本键对排序。
    pairs.sort(key=lambda pair: pair[1])

    assert pairs == [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
