""" 变量

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_variables.asp
@see: https://www.learnpython.org/en/Variables_and_Types

Python是完全面向对象的，而不是“静态类型的”。
在使用变量之前不需要声明变量，也不需要声明变量类型。
Python中的每个变量都是一个对象。

与其他编程语言不同，Python没有命令
声明一个变量。变量在您第一次赋值时就被创建
一个值。

变量可以有一个较短的名称(如x和y)或更具描述性的名称
(年龄、carname total_volume)。

Python变量的规则:
— 变量名必须以字母或下划线开头。
— 变量名不能以数字开头。
— 只能包含字母数字和下划线(A-z、0-9、_)。
- 变量名区分大小写(age, age和age是三个不同的变量)。
"""


def test_variables():
    """测试变量"""

    integer_variable = 5
    string_variable = 'John'

    assert integer_variable == 5
    assert string_variable == 'John'

    variable_with_changed_type = 4  # x 的类型是 int
    variable_with_changed_type = 'Sally'  # x 现在的类型是 str

    assert variable_with_changed_type == 'Sally'
