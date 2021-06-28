"""成员运算符

@see: https://www.w3schools.com/python/python_operators.asp

成员运算符用于测试一个序列是否出现在一个对象中。
"""


def test_membership_operators():
    """成员运算符"""

    # 让我们使用下面的水果列表来说明成员概念。
    fruit_list = ["apple", "banana"]

    # in
    # 如果对象中存在具有指定值的序列，则返回True。

    # 返回True，因为列表中有一个值为“banana”的序列
    assert "banana" in fruit_list

    # not in
    # 如果对象中不存在具有指定值的序列，则返回True

    # 返回True，因为值为"pineapple"的序列不在列表中。
    assert "pineapple" not in fruit_list
