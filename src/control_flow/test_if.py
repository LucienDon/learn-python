"""IF 语句

@see: https://docs.python.org/3/tutorial/controlflow.html

可以有零个或多个elif部分，else部分是可选的。
关键字' elif '是' else if '的缩写，用于避免过度缩进。

在其他语言中 switch ... case 语句是 if … elif … elif … 替代品
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'
