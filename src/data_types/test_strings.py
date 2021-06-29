"""字符串.

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_strings.asp
@see: https://www.w3schools.com/python/python_ref_string.asp

除了数字，Python还可以操作字符串，可以是
用几种方式表达。它们可以用单引号括起来('…')
或者双引号(“…”)，结果相同。
"""

import pytest


def test_string_type():
    """字符串类型"""

    # 双引号字符串。
    name_1 = "John"
    # 带有单引号的字符串。
    name_2 = 'John'
    # 使用不同类型的引号创建的字符串被视为相同的。
    assert name_1 == name_2
    assert isinstance(name_1, str)
    assert isinstance(name_2, str)

    # \ 可以用来转义引号。
    # 使用\'转义单引号或使用双引号代替。
    single_quote_string = 'doesn\'t'
    double_quote_string = "doesn't"

    assert single_quote_string == double_quote_string

    # \ n表示换行符。
    multiline_string = 'First line.\nSecond line.'
    # 如果没有print()，输出中将包含\n。
    # 但是使用print()， \n会产生一个新行。
    assert multiline_string == 'First line.\nSecond line.'

    # 字符串可以被索引，第一个字符的索引为0。
    # 没有单独的字符类型;一个字符就是一个字符串的大小。请注意，因为-0和0是相同的，所以负索引从1开始。
    word = 'Python'
    assert word[0] == 'P'  # 首位字符
    assert word[5] == 'n'  # 第 6个字符。
    assert word[-1] == 'n'  # 最后一个字符.
    assert word[-2] == 'o'  # 倒数第二个的字符。
    assert word[-6] == 'P'  # 倒数第六个 或 正数第1个字符.

    assert isinstance(word[0], str)

    # 除了索引之外，还支持切片. 虽然索引用来获取个别字符，切片可以让您获取子字符串:
    assert word[0:2] == 'Py'  # 从位置0(包括)到位置2(不包括)的字符.
    assert word[2:5] == 'tho'  # 位置2(包括)至位置5(不包括)的字符.

    # 注意开头总是包含在内，而结尾总是被排除在外.
    # 这确保了s[:i] + s[i:]总是等于s:
    assert word[:2] + word[2:] == 'Python'
    assert word[:4] + word[4:] == 'Python'

    # 切片索引具有有用的缺省值; 省略的第一个索引默认为0，被省略的第二索引默认为字符串的大小切片.
    assert word[:2] == 'Py'  # 字符从开始到位置2(不包括).
    assert word[4:] == 'on'  # 从位置4(包括)到末尾的字符.
    assert word[-2:] == 'on'  # 字符从倒数第二(包括)到结尾.

    # 记住切片是如何工作的一种方法是把指标看作指向字符之间的，具有第一个字符的左边缘的
    # 编号0. 然后是字符串n的最后一个字符的右边缘例如，字符的索引为n:
    #
    # +---+---+---+---+---+---+
    #  | P | y | t | h | o | n |
    #  +---+---+---+---+---+---+
    #  0   1   2   3   4   5   6
    # -6  -5  -4  -3  -2  -1

    # 试图使用一个太大的索引将导致一个错误。
    with pytest.raises(Exception):
        not_existing_character = word[42]
        assert not not_existing_character

    # 但是，在使用范围外的片索引时，使用切片会得到很好的处理:
    assert word[4:42] == 'on'
    assert word[42:] == ''

    # Python字符串不能被改变——它们是不可变的。因此，对字符串中的索引位置赋值会导致错误:
    with pytest.raises(Exception):
        # pylint: disable=unsupported-assignment-operation
        word[0] = 'J'

    # 如果您需要一个不同的字符串，您应该创建一个新的:
    assert 'J' + word[1:] == 'Jython'
    assert word[:2] + 'py' == 'Pypy'

    # 内置函数len()返回字符串的长度:
    characters = 'supercalifragilisticexpialidocious'
    assert len(characters) == 34

    # 字符串字面值可以跨多行。一种方法是使用三引号: """...""" 或 '''...'''.
    # 字符串中自动包含行结束符，但可以通过在行结束符中添加\来防止这种情况。
    #
    # 下面的例子:
    multi_line_string = '''\
        First line
        Second line
    '''

    assert multi_line_string == '''\
        First line
        Second line
    '''


def test_string_operators():
    """ 基本运算

    字符串可以用 + 操作符连接(粘在一起)，并用 * 重复连接3次 'un'，接着是'ium'
    """

    assert 3 * 'un' + 'ium' == 'unununium'

    # 'Py' 'thon'
    python = 'Py''thon'
    assert python == 'Python'

    # 当您想要中断长字符串时，这个特性特别有用:
    text = (
        'Put several strings within parentheses '
        'to have them joined together.'
    )
    assert text == 'Put several strings within parentheses to have them joined together.'

    # 如果你想要连接变量或者一个变量和一个字面值，使用+:
    prefix = 'Py'
    assert prefix + 'thon' == 'Python'


def test_string_methods():
    """字符串的方法"""

    hello_world_string = "Hello, World!"

    # strip()方法从开头或结尾删除任何空格.
    string_with_whitespaces = " Hello, World! "
    assert string_with_whitespaces.strip() == "Hello, World!"

    # len()方法返回字符串的长度.
    assert len(hello_world_string) == 13

    # lower()方法返回小写的字符串.
    assert hello_world_string.lower() == 'hello, world!'

    # upper()方法以大写形式返回字符串.
    assert hello_world_string.upper() == 'HELLO, WORLD!'

    # replace()方法将一个字符串替换为另一个字符串.
    assert hello_world_string.replace('H', 'J') == 'Jello, World!'

    # 如果找到分隔符实例，split()方法将字符串分割成子字符串.
    assert hello_world_string.split(',') == ['Hello', ' World!']

    # 将第一个字符转换为大写
    assert 'low letter at the beginning'.capitalize() == 'Low letter at the beginning'

    # 返回指定值在字符串中出现的次数.
    assert 'low letter at the beginning'.count('t') == 4

    # 在字符串中搜索指定的值并返回找到它的位置.
    assert 'Hello, welcome to my world'.find('welcome') == 7

    # 将每个单词的第一个字符转换为大写
    assert 'Welcome to my world'.title() == 'Welcome To My World'

    # 返回一个字符串，其中指定的值被替换为指定的值。
    assert 'I like bananas'.replace('bananas', 'apples') == 'I like apples'

    # 将可迭代对象的元素连接到字符串的末尾.
    my_tuple = ('John', 'Peter', 'Vicky')
    assert ', '.join(my_tuple) == 'John, Peter, Vicky'

    # 如果字符串中的所有字符都是大写，则返回True.
    assert 'ABC'.isupper()
    assert not 'AbC'.isupper()

    # 检查文本中的所有字符是否都是字母.
    assert 'CompanyX'.isalpha()
    assert not 'Company 23'.isalpha()

    # 如果字符串中的所有字符都是数字，则返回True.
    assert '1234'.isdecimal()
    assert not 'a21453'.isdecimal()


def test_string_formatting():
    """字符串格式化.

    通常情况下，比起简单地打印，您希望对输出的格式有更多的控制空格分隔的值。有几种方法可以格式化输出
    """

    # 若要使用格式化字符串字面值，请在字符串的开始引号或三引号之前以 F 或 f 开头。
    # 在这个字符串内部，你可以在 { and } 字符之间编写一个 Python 表达式，它可以引用变量或文字值。
    year = 2018
    event = 'conference'

    assert f'Results of the {year} {event}' == 'Results of the 2018 conference'

    # 字符串的str.format()方法需要更多的手动操作。 您仍将使用{ and }来标记变量将被替换的位置，并可以提供详细的格式化指令,
    # 但是您还需要提供要格式化的信息。
    yes_votes = 42_572_654  # 相当于 42572654
    no_votes = 43_132_495  # 相当于 43132495
    percentage = yes_votes / (yes_votes + no_votes)

    assert '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage) == ' 42572654 YES votes  49.67%'

    # 当您不需要花哨的输出，而只想快速显示一些用于调试的变量时，可以使用repr()或str()函数将任何值转换为字符串。
    # str()函数的目的是返回值的表示，这些值是相当可读的， 而 repr() 的目的是生成解释器可以读取的表示(或者如果没有等效的语法，将强制SyntaxError)。
    # 对于没有特定表示供人类使用的对象，str()将返回与repr()相同的值。.
    # 许多值，如数字或像列表和字典这样的结构，使用这两个函数都有相同的表示。
    # 特别是字符串，有两种不同的表示形式。

    greeting = 'Hello, world.'
    first_num = 10 * 3.25
    second_num = 200 * 200

    assert str(greeting) == 'Hello, world.'
    assert repr(greeting) == "'Hello, world.'"
    assert str(1 / 7) == '0.14285714285714285'

    # repr()的参数可以是任何Python对象:
    assert repr((first_num, second_num, ('spam', 'eggs'))) == "(32.5, 40000, ('spam', 'eggs'))"

    # 格式化的字符串

    # 格式化字符串字面值(也简称f-strings)可以让你在字符串前加上f或f，并将表达式写成{expression}，从而将 Python 表达式的值包含在字符串中。
    # 表达式后面可以有一个可选的格式说明符. 这允许对如何格式化值进行更大的控制. 下面的示例将圆周率四舍五入到小数点后三位。
    pi_value = 3.14159
    assert f'The value of pi is {pi_value:.3f}.' == 'The value of pi is 3.142.'

    # 在':'后面传递一个整数将使该字段成为最小字符数宽。 这对于使列对齐很有用:
    table_data = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    table_string = ''
    for name, phone in table_data.items():
        table_string += f'{name:7}==>{phone:7d}'

    assert table_string == ('Sjoerd ==>   4127'
                            'Jack   ==>   4098'
                            'Dcab   ==>   7678')

    # String format()方法

    # str.format()方法的基本用法如下:
    assert 'We are {} who say "{}!"'.format('knights', 'Ni') == 'We are knights who say "Ni!"'

    # 方括号和其中的字符(称为格式字段)被传递到str.format()方法中的对象替换。
    # 括号中的数字可以用来引用传递给str.format()方法的对象的位置
    assert '{0} and {1}'.format('spam', 'eggs') == 'spam and eggs'
    assert '{1} and {0}'.format('spam', 'eggs') == 'eggs and spam'

    # 如果关键字参数在str.format()方法中使用，则通过参数的名称引用它们的值。
    formatted_string = 'This {food} is {adjective}.'.format(
        food='spam',
        adjective='absolutely horrible'
    )

    assert formatted_string == 'This spam is absolutely horrible.'

    # 位置参数和关键字参数可以任意组合
    formatted_string = 'The story of {0}, {1}, and {other}.'.format(
        'Bill',
        'Manfred',
        other='Georg'
    )

    assert formatted_string == 'The story of Bill, Manfred, and Georg.'

    # 如果你有一个很长的格式字符串，你不想拆分，如果你可以引用变量的名称，而不是位置。
    # 这可以通过简单地传递字典并使用方括号'[]'来访问键来实现

    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    formatted_string = 'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'

    # 这也可以通过使用“**”作为关键字参数传递表来实现。
    formatted_string = 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'
