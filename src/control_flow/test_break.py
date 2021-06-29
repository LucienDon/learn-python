"""break 语句

@see: https://docs.python.org/3/tutorial/controlflow.html

break语句，就像在C中一样，打破了最内层的“for”或“while”循环。
"""


def test_break_statement():
    """break 语句"""

    # 如果我们在0到100的范围内找到了需要的数字，我们就终止循环。
    number_to_be_found = 42
    # 这个变量将记录我们输入“for”循环的次数。
    number_of_iterations = 0

    for number in range(100):
        if number == number_to_be_found:
            # 在这里中断，不要继续循环。
            break
        else:
            number_of_iterations += 1

    # 我们需要确保break语句一旦找到编号就终止了循环。
    assert number_of_iterations == 42
