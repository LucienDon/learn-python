"""pass 语句

@see: https://docs.python.org/3/tutorial/controlflow.html

pass 语句什么也不做。当语法上需要一个语句，但程序不需要任何操作时，可以使用它。
"""


def test_pass_in_function():
    """函数中的PASS语句

    当您处理新代码时，“Pass”可以用作函数或条件体的占位符，使您能够在更抽象的层次上思考。

    下面的pass语句被静默地忽略，但是它使当前的test_pass()函数有效。
    """
    pass


def test_pass_in_loop():
    """pass 循环。

    “Pass”可以在语法上需要一个语句但程序不需要任何操作时使用。例如:
    """

    # pylint: disable=unused-variable
    for number in range(100):
        # 它什么都不做，但是for循环仍然有效。
        pass

    # 上面的例子是完全没用的，但它只是为了说明这个想法。更有用的例子可能是:
    #
    # while True:
    #   pass  # 忙碌等待键盘中断(Ctrl+C)


# pylint: disable=too-few-public-methods
class MyEmptyClass:
    """类的PASS语句

    “传递”通常用于创建最小类，如当前类。
    """
    pass
