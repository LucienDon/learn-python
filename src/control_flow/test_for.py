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

    # If you need to modify the sequence you are iterating over while inside the loop
    # (for example to duplicate selected items), it is recommended that you first make a copy.
    # Iterating over a sequence does not implicitly make a copy. The slice notation makes this
    # especially convenient:
    for word in words[:]:  # Loop over a slice copy of the entire list.
        if len(word) > 6:
            words.insert(0, word)

    print(words)

    # Otherwise with for w in words:, the example would attempt to create an infinite list,
    # inserting defenestrate over and over again.

    assert words == ['defenestrate', 'cat', 'window', 'defenestrate']

    # If you do need to iterate over a sequence of numbers, the built-in function range() comes in
    # handy. It generates arithmetic progressions:
    iterated_numbers = []

    for number in range(5):
        iterated_numbers.append(number)

    assert iterated_numbers == [0, 1, 2, 3, 4]

    # To iterate over the indices of a sequence, you can combine range() and len() as follows:
    words = ['Mary', 'had', 'a', 'little', 'lamb']
    concatenated_string = ''

    # pylint: disable=consider-using-enumerate
    for word_index in range(len(words)):
        concatenated_string += words[word_index] + ' '

    assert concatenated_string == 'Mary had a little lamb '

    # Or simply use enumerate().
    concatenated_string = ''

    for word_index, word in enumerate(words):
        concatenated_string += word + ' '

    assert concatenated_string == 'Mary had a little lamb '

    # When looping through dictionaries, the key and corresponding value can be retrieved at the
    # same time using the items() method.
    knights_names = []
    knights_properties = []

    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for key, value in knights.items():
        knights_names.append(key)
        knights_properties.append(value)

    assert knights_names == ['gallahad', 'robin']
    assert knights_properties == ['the pure', 'the brave']

    # When looping through a sequence, the position index and corresponding value can be retrieved
    # at the same time using the enumerate() function
    indices = []
    values = []
    for index, value in enumerate(['tic', 'tac', 'toe']):
        indices.append(index)
        values.append(value)

    assert indices == [0, 1, 2]
    assert values == ['tic', 'tac', 'toe']

    # To loop over two or more sequences at the same time, the entries can be paired with
    # the zip() function.
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

    If you do need to iterate over a sequence of numbers, the built-in function range() comes in
    handy. It generates arithmetic progressions.

    In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t.
    It is an object which returns the successive items of the desired sequence when you iterate
    over it, but it doesn’t really make the list, thus saving space.

    We say such an object is iterable, that is, suitable as a target for functions and constructs
    that expect something from which they can obtain successive items until the supply is exhausted.
    We have seen that the for statement is such an iterator. The function list() is another; it
    creates lists from iterables:
    """

    assert list(range(5)) == [0, 1, 2, 3, 4]

    # The given end point is never part of the generated sequence; range(10) generates 10 values,
    # the legal indices for items of a sequence of length 10. It is possible to let the range start
    # at another number, or to specify a different increment (even negative; sometimes this is
    # called the ‘step’):

    assert list(range(5, 10)) == [5, 6, 7, 8, 9]
    assert list(range(0, 10, 3)) == [0, 3, 6, 9]
    assert list(range(-10, -100, -30)) == [-10, -40, -70]
