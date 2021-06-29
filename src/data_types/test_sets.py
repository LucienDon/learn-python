""" Set.

@see: https://www.w3schools.com/python/python_sets.asp
@see: https://docs.python.org/3.7/tutorial/datastructures.html#sets

set 是无序且无索引的集合。
在 Python 中，集合是用花括号写的.

集合对象还支持数学运算，如并、交、差和对称差。
"""


def test_sets():
    """Sets"""
    fruits_set = {"apple", "banana", "cherry"}

    assert isinstance(fruits_set, set)

    # 也可以使用set()构造函数来创建集合。
    # 注意双圆括号
    fruits_set_via_constructor = set(("apple", "banana", "cherry"))

    assert isinstance(fruits_set_via_constructor, set)


def test_set_methods():
    """Set methods"""

    fruits_set = {"apple", "banana", "cherry"}

    # 你可以使用“in”语句检查项目是否已设置
    assert "apple" in fruits_set
    assert "pineapple" not in fruits_set

    # 使用len()方法返回项的数量。
    assert len(fruits_set) == 3

    # 您可以使用add()对象方法来添加一个项目.
    fruits_set.add("pineapple")
    assert "pineapple" in fruits_set
    assert len(fruits_set) == 4

    # 使用remove()方法删除一个条目。
    fruits_set.remove("pineapple")
    assert "pineapple" not in fruits_set
    assert len(fruits_set) == 3

    # 演示对两个单词中唯一字母的集合操作:
    first_char_set = set('abracadabra')
    second_char_set = set('alacazam')

    assert first_char_set == {'a', 'r', 'b', 'c', 'd'}  # 第一个单词的唯一字母
    assert second_char_set == {'a', 'l', 'c', 'z', 'm'}  # 第二个单词中唯一的字母

    # 字母在第一个单词中，但不在第二个单词中。
    assert first_char_set - second_char_set == {'r', 'b', 'd'}

    # 第一个单词或第二个单词或两个单词中的字母。
    assert first_char_set | second_char_set == {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

    # 两个单词中常见的字母。
    assert first_char_set & second_char_set == {'a', 'c'}

    # 字母出现在第一个或第二个单词中，但不能同时出现在两个单词中。
    assert first_char_set ^ second_char_set == {'r', 'd', 'b', 'm', 'z', 'l'}

    # 与列表推导式类似，集合推导式也支持:
    word = {char for char in 'abracadabra' if char not in 'abc'}
    assert word == {'r', 'd'}
