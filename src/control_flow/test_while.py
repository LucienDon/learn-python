"""while 语句

@see: https://docs.python.org/3/tutorial/controlflow.html
@see: https://docs.python.org/3/reference/compound_stmts.html#the-while-statement

只要条件保持为真，while循环就会执行。
在Python中，像在C中一样，任何非零整数值都为真;零是错误的。
条件也可以是字符串或列表值，实际上可以是任何序列;任何长度非零的都为真，空序列为假。

示例中使用的测试是一个简单的比较。
标准比较操作符的写法与C中相同:<(小于)、>(大于)、==(等于)、<=(小于或等于)、>=(大于或等于)和!=(不等于)。
"""


def test_while_statement():
    """WHILE statement"""

    # 让我们用 while 循环将这个数提高到某个幂。
    number = 2
    power = 5

    result = 1

    while power > 0:
        result *= number
        power -= 1

    # 2^5 = 32
    assert result == 32
