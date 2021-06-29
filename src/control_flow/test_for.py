"""FOR statement

@see: https://docs.python.org/3/tutorial/controlflow.html

Python 中的 for 语句与您可能在 C 或 Pascal 中使用的语句略有不同。
Python 的 for 语句不是总是迭代数字的等差数列（如在 Pascal 中），也不是让用户能够定义迭代步骤和暂停条件（如 C），
而是迭代任何序列（列表或一个字符串），按照它们在序列中出现的顺序。例如（没有双关语意）：
"""


# pylint: disable=too-many-locals
def test_for_statement():
    """FOR 语句"""

    # 测试一些字符串:
    words = ['cat', 'window', 'defenestrate']
    words_length = 0

    for word in words:
        words_length += len(word)

    # "cat" 长度是 3
    # "window" 长度是 6
    # "defenestrate" 长度是 12
    assert words_length == (3 + 6 + 12)

    # 如果您需要修改在循环内部迭代的序列 (例如，复制选定项),建议您先复印一份。
    # 在序列上迭代不会隐式地生成副本。 切片表示法使得这特别方便:
    for word in words[:]:  # 循环遍历整个列表的切片副本。
        if len(word) > 6:
            words.insert(0, word)

    # 否则，这个例子将尝试创建一个无限列表，并反复插入defenestrate。

    assert words == ['defenestrate', 'cat', 'window', 'defenestrate']

    # 如果确实需要迭代一个数字序列，那么内置函数 range() 可以派上用场。
    # 它生成等差级数:
    iterated_numbers = []

    for number in range(5):
        iterated_numbers.append(number)

    assert iterated_numbers == [0, 1, 2, 3, 4]

    # 要遍历序列的索引，你可以组合 range() 和 len() 如下:
    words = ['Mary', 'had', 'a', 'little', 'lamb']
    concatenated_string = ''

    # pylint: disable=consider-using-enumerate
    for word_index in range(len(words)):
        concatenated_string += words[word_index] + ' '

    assert concatenated_string == 'Mary had a little lamb '

    # 或者简单地使用 enumerate()。
    concatenated_string = ''

    for word_index, word in enumerate(words):
        concatenated_string += word + ' '

    assert concatenated_string == 'Mary had a little lamb '

    # 在遍历字典时，可以使用 items() 方法同时检索键和相应的值。
    knights_names = []
    knights_properties = []

    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for key, value in knights.items():
        knights_names.append(key)
        knights_properties.append(value)

    assert knights_names == ['gallahad', 'robin']
    assert knights_properties == ['the pure', 'the brave']

    # 当循环遍历一个序列时，可以使用 enumerate() 函数同时检索位置索引和相应的值
    indices = []
    values = []
    for index, value in enumerate(['tic', 'tac', 'toe']):
        indices.append(index)
        values.append(value)

    assert indices == [0, 1, 2]
    assert values == ['tic', 'tac', 'toe']

    # 要同时循环两个或多个序列，可以将条目与 zip() 函数配对。
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    combinations = []

    for question, answer in zip(questions, answers):
        combinations.append('What is your {0}?  It is {1}.'.format(question, answer))

    assert combinations == [
        'What is your name?  It is lancelot.',
        'What is your quest?  It is the holy grail.',
        'What is your favorite color?  It is blue.',
    ]


def test_range_function():
    """Range function

    如果确实需要迭代一个数字序列，那么内置函数 range() 可以派上用场。
    它产生等差级数。

    range() 返回的对象在很多方面都表现得像一个列表，但实际上它不是。
    它是一个在迭代时返回所需序列的连续项的对象，但它并不真正构成列表，因此节省了空间。

    我们说这样的对象是可迭代的，也就是说，适合作为函数和构造的目标他们期望能得到一些连续的东西，直到供应耗尽。
    我们已经看到for语句就是这样一个迭代器。函数list()是另一个; 它从可迭代对象中创建列表:
    """

    assert list(range(5)) == [0, 1, 2, 3, 4]

    # 给定的终点从来不是生成序列的一部分; range(10) 生成10个值，即长度为10的序列的合法索引。
    # 可以让范围从另一个数字开始，或指定不同的增量 (甚至负数; 有时这被称为‘step’):

    assert list(range(5, 10)) == [5, 6, 7, 8, 9]
    assert list(range(0, 10, 3)) == [0, 3, 6, 9]
    assert list(range(-10, -100, -30)) == [-10, -40, -70]
