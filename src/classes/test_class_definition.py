"""类定义的语法。

@see: https://docs.python.org/3/tutorial/classes.html

Python 是一种面向对象的编程语言。
Python 中的几乎所有东西都是对象，包括它的属性和方法。
类就像一个对象构造函数，或者创建对象的“蓝图”。
"""


def test_class_definition():
    """类定义"""

    # 类定义，就像函数定义(def语句)一样，必须在它们生效之前执行。(可以将类定义放在if语句的分支中，或者函数中。)

    class GreetingClass:
        """类定义的示例

        该类包含两个公共方法，不包含构造函数。
        """
        name = 'user'

        def say_hello(self):
            """类方法"""
            # self 参数是对类本身的引用，用于访问属于类的变量。
            # 它不一定是self，你可以随便叫它什么，但它必须是类中任何函数的第一个参数。
            return 'Hello ' + self.name

        def say_goodbye(self):
            """Class method."""
            return 'Goodbye ' + self.name

    # 当输入一个类定义时，将创建一个新的命名空间，并将其用作局部作用域，所有对局部变量的赋值都将进入这个新的命名空间。
    # 特别是，函数定义在这里绑定了新函数的名称。

    # 类实例化使用函数表示法。 只需假设类对象是一个返回类的新实例的无参数函数。
    # 例如，下面的代码将创建一个类的新实例，并将该对象赋值给局部变量。
    greeter = GreetingClass()

    assert greeter.say_hello() == 'Hello user'
    assert greeter.say_goodbye() == 'Goodbye user'
