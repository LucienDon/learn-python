"""错误和异常。

@see: https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions

即使一个语句或表达式在语法上是正确的，在尝试执行它时也可能会导致错误。
在执行过程中检测到的错误称为异常，并不是无条件致命的。

编写处理选定异常的程序是可能的。
"""


def test_handle_exceptions():
    """Handling of exceptions

    try语句的工作原理如下。

    - 首先，执行try子句(try和except关键字之间的语句)。

    - 如果没有异常发生，则跳过except子句，并结束try语句的执行。

    - 如果在try子句执行期间发生异常，则跳过子句的其余部分。
    然后，如果它的类型与except关键字后面命名的异常匹配，则执行except子句，然后在try语句之后继续执行。

    - 如果发生了与except子句中指定的异常不匹配的异常，则将其传递给外部的try语句;
    如果没有找到处理程序，则这是一个未处理的异常，执行将以一条消息停止。
    """

    # 让我们来模拟除零异常。
    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # 除以零
        # 我们根本就不该来这里。
        assert result
    except ZeroDivisionError:
        # 我们应该到这里，因为除以0。
        exception_has_been_handled = True

    assert exception_has_been_handled

    # 让我们模拟未定义变量访问异常。
    exception_has_been_handled = False
    try:
        # pylint: disable=undefined-variable
        result = 4 + spam * 3  # 名称“spam”没有定义
        # 我们根本就不该来这里。
        assert result
    except NameError:
        exception_has_been_handled = True

    assert exception_has_been_handled

    # 一个try语句可以有多个except子句，用于指定不同异常的处理程序。
    # 最多将执行一个处理程序。处理程序只处理相应的try子句中发生的异常，而不处理同一try语句的其他处理程序中发生的异常。
    # except子句可以将多个异常命名为带括号的元组，例如:

    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # division by zero
        # 我们根本就不该来这里。
        assert result
    except (ZeroDivisionError, NameError):
        # 我们应该到这里，因为除以0。
        exception_has_been_handled = True

    assert exception_has_been_handled

    # 异常处理程序可以被链接。
    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # 除以零
        # 我们根本就不该来这里。
        assert result
    except NameError:
        # 我们应该到这里，因为除以0。
        exception_has_been_handled = True
    except ZeroDivisionError:
        # 我们应该到这里，因为除以0。
        exception_has_been_handled = True

    assert exception_has_been_handled

    # try…except语句有一个可选的else子句，当它出现时，必须跟在所有except子句后面。
    # 对于在try子句没有引发异常时必须执行的代码，它是有用的。例如:

    exception_has_been_handled = False
    no_exceptions_has_been_fired = False

    try:
        result = 10
        # 我们根本就不该来这里。
        assert result
    except NameError:
        # 我们应该到这里，因为除以0。
        exception_has_been_handled = True
    else:
        no_exceptions_has_been_fired = True

    assert not exception_has_been_handled
    assert no_exceptions_has_been_fired
