"""字典.

@see: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
@see: https://www.w3schools.com/python/python_dictionaries.asp

字典是无序的、可变的和有索引的集合。
在 Python 中，字典是用大括号写的，它们有键和值。

在其他语言中，词典有时被称为“联想记忆”或“联想记忆”数组”。
与序列(由一系列数字建立索引)不同，字典通过键建立索引，键可以是任何不可变类型;
字符串和数字总是可以作为键. 如果元组只包含字符串、数字或元组，则可以用作键;如果一个元组包含任何可变对象它不能直接或间接地作为键使用.
不能将列表用作键，因为可以使用索引赋值、切片赋值或 append() 和 extend() 等方法在适当的位置修改列表。

最好把字典看作是一组键: 值对, 有了这个要求键是唯一的(在一个字典中)。
一对大括号创建一个空字典:{}。
在花括号中放置一个逗号分隔的键:值对列表，将初始键:值对添加到字典中;这也是在输出上编写字典的方式。
"""


def test_dictionary():
    """Dictionary"""

    fruits_dictionary = {
        'cherry': 'red',
        'apple': 'green',
        'banana': 'yellow',
    }

    assert isinstance(fruits_dictionary, dict)

    # 你可以通过键来访问集合元素。
    assert fruits_dictionary['apple'] == 'green'
    assert fruits_dictionary['banana'] == 'yellow'
    assert fruits_dictionary['cherry'] == 'red'

    # 若要检查字典中是否有单个键，请使用in关键字。
    assert 'apple' in fruits_dictionary
    assert 'pineapple' not in fruits_dictionary

    # 改变苹果的颜色为“红色”。
    fruits_dictionary['apple'] = 'red'

    # 向字典中添加新的键值对
    fruits_dictionary['pineapple'] = 'yellow'
    assert fruits_dictionary['pineapple'] == 'yellow'

    # 对一个字典执行list(d)将返回一个包含该字典中使用的所有键的列表，按插入顺序(如果您想要对其排序，只需使用sorted(d))。
    assert list(fruits_dictionary) == ['cherry', 'apple', 'banana', 'pineapple']
    assert sorted(fruits_dictionary) == ['apple', 'banana', 'cherry', 'pineapple']

    # 也可以用del删除键值对。
    del fruits_dictionary['pineapple']
    assert list(fruits_dictionary) == ['cherry', 'apple', 'banana']

    # dict()构造函数直接从键-值对序列构建字典。
    dictionary_via_constructor = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

    assert dictionary_via_constructor['sape'] == 4139
    assert dictionary_via_constructor['guido'] == 4127
    assert dictionary_via_constructor['jack'] == 4098

    # 此外，字典推导式可以用于从任意键和值表达式创建字典:
    dictionary_via_expression = {x: x ** 2 for x in (2, 4, 6)}
    assert dictionary_via_expression[2] == 4
    assert dictionary_via_expression[4] == 16
    assert dictionary_via_expression[6] == 36

    # 当键是简单字符串时，使用关键字参数指定键对有时会更容易。
    dictionary_for_string_keys = dict(sape=4139, guido=4127, jack=4098)
    assert dictionary_for_string_keys['sape'] == 4139
    assert dictionary_for_string_keys['guido'] == 4127
    assert dictionary_for_string_keys['jack'] == 4098
