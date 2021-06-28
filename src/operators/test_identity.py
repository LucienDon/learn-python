"""恒等运算符

@see: https://www.w3schools.com/python/python_operators.asp

恒等运算符用于比较对象，不是比较它们是否相等，而是比较它们是否相等
相同的对象，相同的内存位置。
"""


def test_identity_operators():
    """恒等运算符"""

    # 让我们根据下面的列表演示恒等运算符。
    first_fruits_list = ["apple", "banana"]
    second_fruits_list = ["apple", "banana"]
    third_fruits_list = first_fruits_list

    # is
    # 如果两个变量是同一个对象，则返回true.

    # Example:
    # First_fruits_list和third_fruits_list是相同的对象。
    assert first_fruits_list is third_fruits_list

    # is not
    # 如果两个变量不是同一个对象，则返回true。

    # Example:
    # First_fruits_list和second_fruits_list不是相同的对象，即使它们有相同的内容
    assert first_fruits_list is not second_fruits_list

    # 为了演示"is"和"=="之间的区别:这个比较返回True因为First_fruits_list等于second_fruits_list。
    assert first_fruits_list == second_fruits_list
