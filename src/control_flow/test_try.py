"""try 语句

@see: https://www.w3schools.com/python/python_try_except.asp

"try" 语句被用于异常处理.
当出现错误或我们所说的异常时，Python通常会停止并生成错误消息。这些异常可以使用try语句来处理。

“try” 块允许您测试代码块的错误。
“except” 块允许您处理错误。
"else" 块允许您在没有引发错误的情况下执行代码。
“finally” 块允许您执行代码，而不管try的结果如何——除了块之外。
"""


def test_try():
    """TRY statement"""

    # try块将产生一个错误，因为 not_existing_variable 没有定义:
    exception_has_been_caught = False

    try:
        # pylint: disable=undefined-variable
        print(not_existing_variable)
    except NameError:
        exception_has_been_caught = True

    assert exception_has_been_caught

    # 你可以定义任意多的异常块，例如，如果你想为一个特殊的错误执行一个特殊的代码块:
    exception_message = ''

    try:
        # pylint: disable=undefined-variable
        print(not_existing_variable)
    except NameError:
        exception_message = 'Variable is not defined'

    assert exception_message == 'Variable is not defined'

    # 如果未引发错误，可以使用else关键字定义要执行的代码块。
    message = ''
    # pylint: disable=broad-except
    try:
        message += 'Success.'
    except NameError:
        message += 'Something went wrong.'
    else:
        message += 'Nothing went wrong.'

    assert message == 'Success.Nothing went wrong.'

    # 如果指定了 finally 块，则无论try块是否引发错误都将执行。
    message = ''
    try:
        # pylint: undefined-variable
        print(not_existing_variable)  # noqa: F821
    except NameError:
        message += 'Something went wrong.'
    finally:
        message += 'The "try except" is finished.'

    assert message == 'Something went wrong.The "try except" is finished.'
