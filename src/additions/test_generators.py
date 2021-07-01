"""Generators.

@see: https://www.learnpython.org/en/Generators

生成器用于创建迭代器，但采用了不同的方法。生成器是一个简单的函数，它以一种特殊的方式每次返回一个可迭代的项集。

当使用for语句开始对一组项进行迭代时，将运行生成器。
一旦生成器的函数代码到达“yield”语句， 生成器将其执行返回给for循环，并从集合返回一个新值。
生成器函数可以生成任意多的值(可能是无限)，并依次生成每个值。
"""

import random


def lottery():
    """生成器函数的例子。

    下面是一个返回随机整数的生成器函数的简单示例。
    这个函数决定如何自己生成随机数， 一次一个地执行yield语句， 在两个循环之间暂停，使执行返回主for循环。
    """
    # 返回1到10之间的前3个随机数字
    # pylint: disable=unused-variable
    for i in range(3):
        yield random.randint(1, 10)

    # 返回10到20之间的第4个数字
    yield random.randint(10, 20)


def test_generators():
    """Yield statement"""
    for number_index, random_number in enumerate(lottery()):
        if number_index < 3:
            assert 0 <= random_number <= 10
        else:
            assert 10 <= random_number <= 20
