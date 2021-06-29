"""列表

# @see: https://www.learnpython.org/en/Lists
# @see: https://docs.python.org/3/tutorial/introduction.html
# @ee: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

Python 知道许多用于组合的复合数据类型其他值。
最通用的是列表，可以写成 a 方括号之间用逗号分隔的值(项)列表。
列表可能包含不同类型的项，但通常所有项都有相同的类型.
"""

import pytest


def test_list_type():
    """列表类型."""

    # 列表非常类似于数组. 它们可以包含任何类型的变量，并且可以包含任意多的变量.
    # 列表也可以以一种非常简单的方式迭代.
    # 下面是一个如何构建列表的示例。
    squares = [1, 4, 9, 16, 25]

    assert isinstance(squares, list)

    # 和字符串(以及所有其他内置序列类型)一样，列表也可以被索引和切片:
    assert squares[0] == 1  # 索引返回项
    assert squares[-1] == 25
    assert squares[-3:] == [9, 16, 25]  # slice 返回一个新列表

    # 所有切片操作都返回一个包含所请求元素的新列表。
    # 这意味着下面的切片返回列表的一个新(浅)副本:
    assert squares[:] == [1, 4, 9, 16, 25]

    # 列表也支持像连接这样的操作:
    assert squares + [36, 49, 64, 81, 100] == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # 与不可变的字符串不同，列表是一种可变类型。
    # 可以改变它们的内容:
    cubes = [1, 8, 27, 65, 125]  # 这里有问题，4的 3 次方是64!
    cubes[3] = 64  # 替换错误的值
    assert cubes == [1, 8, 27, 64, 125]

    # 还可以使用append()方法在列表末尾添加新项
    cubes.append(216)  # 添加 6的立方
    cubes.append(7 ** 3)  # 添加 7的立方
    assert cubes == [1, 8, 27, 64, 125, 216, 343]

    # 也可以给切片赋值，这甚至可以改变列表的大小或完全清除它:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    letters[2:5] = ['C', 'D', 'E']  # 替换一些值
    assert letters == ['a', 'b', 'C', 'D', 'E', 'f', 'g']
    letters[2:5] = []  # 现在删除它们
    assert letters == ['a', 'b', 'f', 'g']
    # 通过将所有元素替换为空列表来清除列表
    letters[:] = []
    assert letters == []

    # 内置函数len()也适用于列表
    letters = ['a', 'b', 'c', 'd']
    assert len(letters) == 4

    # 可以嵌套列表(创建包含其他列表的列表),
    # 例如:
    list_of_chars = ['a', 'b', 'c']
    list_of_numbers = [1, 2, 3]
    mixed_list = [list_of_chars, list_of_numbers]
    assert mixed_list == [['a', 'b', 'c'], [1, 2, 3]]
    assert mixed_list[0] == ['a', 'b', 'c']
    assert mixed_list[0][1] == 'b'


def test_list_methods():
    """测试列表的方法。"""

    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.append(x)
    # 将一个项目添加到列表的末尾。
    # 相当于 a[len(a):] = [x].
    fruits.append('grape')
    assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape']

    # list.remove(x)
    # 从列表中删除值为x的第一项.
    # 如果没有这样的项，它将引发ValueError。
    fruits.remove('grape')
    assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    with pytest.raises(Exception):
        fruits.remove('not existing element')

    # list.insert(i, x)
    # 在给定位置插入一项。
    # 第一个参数是要插入的元素的索引，所以 a.insert(0, x) 插入到列表的前面，而 a.insert(len(a), x) 等价于 a.append(x)。
    fruits.insert(0, 'grape')
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.index(x[, start[, end]])
    # 返回值为x的第一个项的列表中从0开始的索引。
    # 如果没有这样的项则引发ValueError。
    # 可选参数 start 和 end 被解释为切片表示法，用于将搜索限制为列表的特定子序列。
    # 返回计算的索引
    # 相对于整个序列的开始，而不是start参数。
    assert fruits.index('grape') == 0
    assert fruits.index('orange') == 1
    assert fruits.index('banana') == 4
    assert fruits.index('banana', 5) == 7  # 找到下一个 banana 开始位置 5

    with pytest.raises(Exception):
        fruits.index('not existing element')

    # list.count(x)
    # 返回 x 出现在列表中的次数。
    assert fruits.count('tangerine') == 0
    assert fruits.count('banana') == 2

    # list.copy()
    # 返回列表的浅拷贝。 相当于 a[:].
    fruits_copy = fruits.copy()
    assert fruits_copy == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.reverse()
    # 将列表中的元素反向排列。
    fruits_copy.reverse()
    assert fruits_copy == [
        'banana',
        'apple',
        'kiwi',
        'banana',
        'pear',
        'apple',
        'orange',
        'grape',
    ]

    # list.sort(key=None, reverse=False)
    # 对列表中的项进行适当排序(参数可用于排序定制，请参阅 sorted() 了解它们的解释)。
    fruits_copy.sort()
    assert fruits_copy == [
        'apple',
        'apple',
        'banana',
        'banana',
        'grape',
        'kiwi',
        'orange',
        'pear',
    ]

    # list.pop([i])
    # 删除列表中给定位置的项，并返回它。如果没有指定索引，a.pop()将删除并返回列表中的最后一项。
    # (方法签名中i周围的方括号表示参数是可选的，而不是在那个位置输入方括号。)
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    assert fruits.pop() == 'banana'
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']

    # list.clear()
    # 从列表中删除所有项目。 相当于 del a[:].
    fruits.clear()
    assert fruits == []


def test_del_statement():
    """del 语法

    有一种方法可以从列表中删除给定索引而不是值的项: del.
    这与有返回值的 pop()方法不同。 del语句还可以用于从列表中删除片或清除整个列表 (我们之前是通过给切片赋一个空列表来做的).
    """

    numbers = [-1, 1, 66.25, 333, 333, 1234.5]

    del numbers[0]
    assert numbers == [1, 66.25, 333, 333, 1234.5]

    del numbers[2:4]
    assert numbers == [1, 66.25, 1234.5]

    del numbers[:]
    assert numbers == []

    # del 也可以用来删除整个变量:
    del numbers
    with pytest.raises(Exception):
        # 之后引用名称 numbers 是错误的 (至少在给它赋值之前是这样).
        assert numbers == []  # noqa: F821


def test_list_comprehensions():
    """列表推导式.

    列表推导式提供了一种创建列表的简明方法。 常见的应用是使新列出每个元素是应用于另一个元素的每个成员的某些操作的结果序列或可迭代的，
    或创建满足一定条件的那些元素的子序列条件。

    列表推导式由括号组成，括号中包含一个表达式，后面跟着一个 for 子句，然后零个或多个 for 或 if 子句。
    结果将是一个新的列表，它是在表达式后面的 for 和 if 子句的上下文中对表达式求值而得到的。
    """

    # 例如，假设我们想要创建一个正方形列表，
    # 请注意，这将创建(或覆盖)一个名为“number”的变量，该变量在循环完成后仍然存在。
    # 例如:
    squares = []
    for number in range(10):
        squares.append(number ** 2)

    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 我们可以在没有任何副作用的情况下计算方块列表:
    squares = list(map(lambda x: x ** 2, range(10)))
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 或者，同样的(更简洁易读):
    squares = [x ** 2 for x in range(10)]
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 例如，如果两个列表的元素不相等，这个 listcomp 将组合它们。
    combinations = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    # 它等价于
    combinations = []
    for first_number in [1, 2, 3]:
        for second_number in [3, 1, 4]:
            if first_number != second_number:
                combinations.append((first_number, second_number))

    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    # 注意，这两个代码片段中的for和if语句的顺序是相同的.

    # 如果表达式是一个元组(例如前面例子中的(x, y))，则必须用圆括号括起来。

    # 让我们来看更多的例子:

    vector = [-4, -2, 0, 2, 4]

    # 创建一个值翻倍的新列表。
    doubled_vector = [x * 2 for x in vector]
    assert doubled_vector == [-8, -4, 0, 4, 8]

    # 过滤列表以排除负数。
    positive_vector = [x for x in vector if x >= 0]
    assert positive_vector == [0, 2, 4]

    # 对所有元素应用一个函数。
    abs_vector = [abs(x) for x in vector]
    assert abs_vector == [4, 2, 0, 2, 4]

    # 对每个元素调用一个方法。
    fresh_fruit = ['  banana', '  loganberry ', 'passion fruit  ']
    clean_fresh_fruit = [weapon.strip() for weapon in fresh_fruit]
    assert clean_fresh_fruit == ['banana', 'loganberry', 'passion fruit']

    # 创建一个2元组列表，如(number, square).
    square_tuples = [(x, x ** 2) for x in range(6)]
    assert square_tuples == [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

    # 使用带有两个 for 的列表组合使列表变平.
    vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flatten_vector = [num for elem in vector for num in elem]
    assert flatten_vector == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_nested_list_comprehensions():
    """嵌套列表推导式1
    列表推导式中的初始表达式可以是任意表达式，包括另一个corrrmprehension列表。
    """

    # 考虑下面这个3x4矩阵的例子，它是一个由3个长度为4的列表组成的列表:
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    # 下面的列表推导式将对行和列进行转置:
    transposed_matrix = [[row[i] for row in matrix] for i in range(4)]
    assert transposed_matrix == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # 正如我们在前一节中看到的，嵌套的listcomp是在它后面的for上下文中求值的, 所以这个例子相当于:
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])

    assert transposed == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # 反过来，也就是:
    transposed = []
    for i in range(4):
        # 下面的3行实现了嵌套的listcomp
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)

    assert transposed == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # 在现实世界中，您应该更喜欢内置函数而不是复杂的流语句。
    # zip()函数可以很好地完成这个用例:
    assert list(zip(*matrix)) == [
        (1, 5, 9),
        (2, 6, 10),
        (3, 7, 11),
        (4, 8, 12),
    ]
