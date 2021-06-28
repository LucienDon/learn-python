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

    # Attempting to use an index that is too large will result in an error.
    with pytest.raises(Exception):
        not_existing_character = word[42]
        assert not not_existing_character

    # However, out of range slice indexes are handled gracefully when used
    # for slicing:
    assert word[4:42] == 'on'
    assert word[42:] == ''

    # Python strings cannot be changed — they are immutable. Therefore,
    # assigning to an indexed position in the string
    # results in an error:
    with pytest.raises(Exception):
        # pylint: disable=unsupported-assignment-operation
        word[0] = 'J'

    # If you need a different string, you should create a new one:
    assert 'J' + word[1:] == 'Jython'
    assert word[:2] + 'py' == 'Pypy'

    # The built-in function len() returns the length of a string:
    characters = 'supercalifragilisticexpialidocious'
    assert len(characters) == 34

    # String literals can span multiple lines. One way is using triple-quotes: """..."""
    # or '''...'''. End of lines are automatically included in the string, but it’s possible
    # to prevent this by adding a \ at the end of the line. The following example:
    multi_line_string = '''\
        First line
        Second line
    '''

    assert multi_line_string == '''\
        First line
        Second line
    '''


def test_string_operators():
    """Basic operations

    Strings can be concatenated (glued together) with the + operator,
    and repeated with *: 3 times 'un', followed by 'ium'
    """

    assert 3 * 'un' + 'ium' == 'unununium'

    # 'Py' 'thon'
    python = 'Py' 'thon'
    assert python == 'Python'

    # This feature is particularly useful when you want to break long strings:
    text = (
        'Put several strings within parentheses '
        'to have them joined together.'
    )
    assert text == 'Put several strings within parentheses to have them joined together.'

    # If you want to concatenate variables or a variable and a literal, use +:
    prefix = 'Py'
    assert prefix + 'thon' == 'Python'


def test_string_methods():
    """String methods"""

    hello_world_string = "Hello, World!"

    # The strip() method removes any whitespace from the beginning or the end.
    string_with_whitespaces = " Hello, World! "
    assert string_with_whitespaces.strip() == "Hello, World!"

    # The len() method returns the length of a string.
    assert len(hello_world_string) == 13

    # The lower() method returns the string in lower case.
    assert hello_world_string.lower() == 'hello, world!'

    # The upper() method returns the string in upper case.
    assert hello_world_string.upper() == 'HELLO, WORLD!'

    # The replace() method replaces a string with another string.
    assert hello_world_string.replace('H', 'J') == 'Jello, World!'

    # The split() method splits the string into substrings if it finds instances of the separator.
    assert hello_world_string.split(',') == ['Hello', ' World!']

    # Converts the first character to upper case
    assert 'low letter at the beginning'.capitalize() == 'Low letter at the beginning'

    # Returns the number of times a specified value occurs in a string.
    assert 'low letter at the beginning'.count('t') == 4

    # Searches the string for a specified value and returns the position of where it was found.
    assert 'Hello, welcome to my world'.find('welcome') == 7

    # Converts the first character of each word to upper case
    assert 'Welcome to my world'.title() == 'Welcome To My World'

    # Returns a string where a specified value is replaced with a specified value.
    assert 'I like bananas'.replace('bananas', 'apples') == 'I like apples'

    # Joins the elements of an iterable to the end of the string.
    my_tuple = ('John', 'Peter', 'Vicky')
    assert ', '.join(my_tuple) == 'John, Peter, Vicky'

    # Returns True if all characters in the string are upper case.
    assert 'ABC'.isupper()
    assert not 'AbC'.isupper()

    # Check if all the characters in the text are letters.
    assert 'CompanyX'.isalpha()
    assert not 'Company 23'.isalpha()

    # Returns True if all characters in the string are decimals.
    assert '1234'.isdecimal()
    assert not 'a21453'.isdecimal()


def test_string_formatting():
    """String formatting.

    Often you’ll want more control over the formatting of your output than simply printing
    space-separated values. There are several ways to format output
    """

    # To use formatted string literals, begin a string with f or F before the opening quotation
    # mark or triple quotation mark. Inside this string, you can write a Python expression
    # between { and } characters that can refer to variables or literal values.
    year = 2018
    event = 'conference'

    assert f'Results of the {year} {event}' == 'Results of the 2018 conference'

    # The str.format() method of strings requires more manual effort. You’ll still use { and } to
    # mark where a variable will be substituted and can provide detailed formatting directives,
    # but you’ll also need to provide the information to be formatted.
    yes_votes = 42_572_654  # equivalent of 42572654
    no_votes = 43_132_495   # equivalent of 43132495
    percentage = yes_votes / (yes_votes + no_votes)

    assert '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage) == ' 42572654 YES votes  49.67%'

    # When you don’t need fancy output but just want a quick display of some variables for debugging
    # purposes, you can convert any value to a string with the repr() or str() functions. The str()
    # function is meant to return representations of values which are fairly human-readable, while
    # repr() is meant to generate representations which can be read by the interpreter (or will
    # force a SyntaxError if there is no equivalent syntax). For objects which don’t have a
    # particular representation for human consumption, str() will return the same value as repr().
    # Many values, such as numbers or structures like lists and dictionaries, have the same
    # representation using either function. Strings, in particular, have two distinct
    # representations.

    greeting = 'Hello, world.'
    first_num = 10 * 3.25
    second_num = 200 * 200

    assert str(greeting) == 'Hello, world.'
    assert repr(greeting) == "'Hello, world.'"
    assert str(1/7) == '0.14285714285714285'

    # The argument to repr() may be any Python object:
    assert repr((first_num, second_num, ('spam', 'eggs'))) == "(32.5, 40000, ('spam', 'eggs'))"

    # Formatted String Literals

    # Formatted string literals (also called f-strings for short) let you include the value of
    # Python expressions inside a string by prefixing the string with f or F and writing
    # expressions as {expression}.

    # An optional format specifier can follow the expression. This allows greater control over how
    # the value is formatted. The following example rounds pi to three places after the decimal.
    pi_value = 3.14159
    assert f'The value of pi is {pi_value:.3f}.' == 'The value of pi is 3.142.'

    # Passing an integer after the ':' will cause that field to be a minimum number of characters
    # wide. This is useful for making columns line up:
    table_data = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    table_string = ''
    for name, phone in table_data.items():
        table_string += f'{name:7}==>{phone:7d}'

    assert table_string == ('Sjoerd ==>   4127'
                            'Jack   ==>   4098'
                            'Dcab   ==>   7678')

    # The String format() Method

    # Basic usage of the str.format() method looks like this:
    assert 'We are {} who say "{}!"'.format('knights', 'Ni') == 'We are knights who say "Ni!"'

    # The brackets and characters within them (called format fields) are replaced with the objects
    # passed into the str.format() method. A number in the brackets can be used to refer to the
    # position of the object passed into the str.format() method
    assert '{0} and {1}'.format('spam', 'eggs') == 'spam and eggs'
    assert '{1} and {0}'.format('spam', 'eggs') == 'eggs and spam'

    # If keyword arguments are used in the str.format() method, their values are referred to by
    # using the name of the argument.
    formatted_string = 'This {food} is {adjective}.'.format(
        food='spam',
        adjective='absolutely horrible'
    )

    assert formatted_string == 'This spam is absolutely horrible.'

    # Positional and keyword arguments can be arbitrarily combined
    formatted_string = 'The story of {0}, {1}, and {other}.'.format(
        'Bill',
        'Manfred',
        other='Georg'
    )

    assert formatted_string == 'The story of Bill, Manfred, and Georg.'

    # If you have a really long format string that you don’t want to split up, it would be nice if
    # you could reference the variables to be formatted by name instead of by position. This can be
    # done by simply passing the dict and using square brackets '[]' to access the keys

    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    formatted_string = 'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'

    # This could also be done by passing the table as keyword arguments with the ‘**’ notation.
    formatted_string = 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'
