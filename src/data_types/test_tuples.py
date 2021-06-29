""" 元组.

@see: https://www.w3schools.com/python/python_tuples.asp
@see: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

元组是有序且不可更改的集合。 在Python中，元组是用圆括弧。

元组有以下属性:
- 不能更改元组中的值。
- 不能删除元组中的项。
"""

import pytest


def test_tuples():
    """ 元组"""
    fruits_tuple = ("apple", "banana", "cherry")

    assert isinstance(fruits_tuple, tuple)
    assert fruits_tuple[0] == "apple"
    assert fruits_tuple[1] == "banana"
    assert fruits_tuple[2] == "cherry"

    # 不能更改元组中的值。
    with pytest.raises(Exception):
        # pylint: disable=unsupported-assignment-operation
        fruits_tuple[0] = "pineapple"

    # 也可以使用 tuple() 构造函数来创建一个元组 (注意两个圆括号)。
    # len()函数返回元组的长度。
    fruits_tuple_via_constructor = tuple(("apple", "banana", "cherry"))

    assert isinstance(fruits_tuple_via_constructor, tuple)
    assert len(fruits_tuple_via_constructor) == 3

    # 初始化元组时也可以省略括号。
    another_tuple = 12345, 54321, 'hello!'
    assert another_tuple == (12345, 54321, 'hello!')

    # 元组可以嵌套:
    nested_tuple = another_tuple, (1, 2, 3, 4, 5)
    assert nested_tuple == ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

    # 如您所见，在输出时元组总是括在括号中，因此嵌套的元组是正确解读;
    # 它们的输入可以带或不带圆括号，尽管圆括号通常是必须的(如果元组是一个更大的表达式的一部分).
    # 不能为元组的单个项赋值，但是可以创建包含可变对象的元组，比如列表。

    # 一个特殊的问题是包含0或1项的元组的构造: 语法有一些额外的怪癖来适应这些。
    # 空元组由一对空括号构成;
    # 只有一项的元组是通过在值后面加逗号来构造的(将单个值括在圆括号中是不够的).
    # 丑,但有效。例如:
    empty_tuple = ()
    # pylint: disable=len-as-condition
    assert len(empty_tuple) == 0

    # pylint: disable=trailing-comma-tuple
    singleton_tuple = 'hello',  # <-- 注意后面的逗号
    assert len(singleton_tuple) == 1
    assert singleton_tuple == ('hello',)

    # 下面的例子被称为元组打包:
    packed_tuple = 12345, 54321, 'hello!'

    # 反向操作也是可以的。
    first_tuple_number, second_tuple_number, third_tuple_string = packed_tuple
    assert first_tuple_number == 12345
    assert second_tuple_number == 54321
    assert third_tuple_string == 'hello!'

    # 这被称为序列解包，并适用于右边的任何序列。
    # 序列解包要求等号左边的变量数量与序列中的元素数量相等。
    # 请注意，多重赋值实际上只是元组打包和序列解包的组合。

    # 交换使用元组。
    # 数据可以在 python 中使用
    # 元组。这样就不需要使用'temp'变量了。
    first_number = 123
    second_number = 456
    first_number, second_number = second_number, first_number

    assert first_number == 456
    assert second_number == 123
