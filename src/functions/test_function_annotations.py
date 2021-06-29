"""函数注释。

@see: https://docs.python.org/3/tutorial/controlflow.html#function-annotations

函数注释是关于用户定义函数使用的类型的完全可选的元数据信息。

注释作为字典存储在函数的__annotations__属性中，对函数的任何其他部分都没有影响。 参数注释通过参数名称后面的冒号定义，后面是求值为注释值的表达式。
返回注释由文字定义 ->, 后面是一个表达式，在形参表和表示 def 语句结束的冒号之间。
"""


def breakfast(ham: str, eggs: str = 'eggs') -> str:
    """Breakfast creator.

    这个函数有一个位置参数、一个关键字参数和带注释的返回值。
    """
    return ham + ' and ' + eggs


def test_function_annotations():
    """函数注释。"""

    assert breakfast.__annotations__ == {'eggs': str, 'ham': str, 'return': str}
