"""提高异常。

@see: https://docs.python.org/3/tutorial/errors.html#raising-exceptions

raise 语句允许程序员强制发生指定的异常。
"""


def test_raise_exception():
    """提高异常。

    raise语句允许程序员强制发生指定的异常。
    """
    exception_is_caught = False

    try:
        # 要引发的唯一参数表示要引发的异常。
        # 这必须是异常实例或异常类(派生自exception的类)。
        # 如果传递了一个异常类，它将通过调用不带参数的构造函数隐式实例化
        raise NameError('HiThere')  # 'raise ValueError()'的简写
    except NameError:
        exception_is_caught = True

    assert exception_is_caught


def test_user_defined_exception():
    """用户自定义异常"""

    # 程序可以通过创建一个新的异常类来命名自己的异常。
    # 异常通常应该直接或间接地派生自Exception类。
    # 大多数异常的名称都以“Error”结尾，类似于标准异常的命名。
    # 许多标准模块定义了它们自己的异常，以报告它们定义的函数中可能发生的错误。
    class MyCustomError(Exception):
        """MyCustomError异常示例。"""

        def __init__(self, message):
            super().__init__(message)
            self.message = message

    try:
        raise MyCustomError('My custom message')
    except MyCustomError:

        custom_exception_is_caught = True

    assert custom_exception_is_caught
