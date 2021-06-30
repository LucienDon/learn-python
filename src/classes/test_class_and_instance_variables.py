"""类和实例变量。

@see: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables

一般来说，实例变量用于每个实例唯一的数据，类变量用于类的所有实例共享的属性和方法。
"""


def test_class_and_instance_variables():
    """类和实例变量。"""

    # pylint: disable=too-few-public-methods
    class Dog:
        """Dog class example"""
        kind = 'canine'  # 所有实例共享的类变量.

        def __init__(self, name):
            self.name = name  # 实例变量对每个实例是唯一的。

    fido = Dog('Fido')
    buddy = Dog('Buddy')

    # 所有的狗都有。
    assert fido.kind == 'canine'
    assert buddy.kind == 'canine'

    # fido 独有。
    assert fido.name == 'Fido'

    # buddy 独有。
    assert buddy.name == 'Buddy'

    # 如果涉及到诸如列表和字典之类的可变对象，共享数据可能会产生令人惊讶的效果。
    # 例如，以下代码中的 tricks 列表不应该用作类变量，因为所有 Dog 实例只共享一个列表。

    # pylint: disable=too-few-public-methods
    class DogWithSharedTricks:
        """共享变量使用错误的 Dog 类例子"""
        tricks = []  # 错误地将类变量用于可变对象(见下文)。

        def __init__(self, name):
            self.name = name  # 实例变量对每个实例是唯一的。

        def add_trick(self, trick):
            """Add trick to the dog

            这个函数说明了可变类变量的错误使用(见下文)。
            """
            self.tricks.append(trick)

    fido = DogWithSharedTricks('Fido')
    buddy = DogWithSharedTricks('Buddy')

    fido.add_trick('roll over')
    buddy.add_trick('play dead')

    assert fido.tricks == ['roll over', 'play dead']  # 没想到所有的 Dog 都有
    assert buddy.tricks == ['roll over', 'play dead']  # 没想到所有的 Dog 都有

    # 正确的类设计应该使用实例变量:

    # pylint: disable=too-few-public-methods
    class DogWithTricks:
        """Dog class example"""

        def __init__(self, name):
            self.name = name  # 实例变量对每个实例是唯一的。
            self.tricks = []  # 为每只狗创建一个新的空列表

        def add_trick(self, trick):
            """Add trick to the dog
            """
            self.tricks.append(trick)

    fido = DogWithTricks('Fido')
    buddy = DogWithTricks('Buddy')

    fido.add_trick('roll over')
    buddy.add_trick('play dead')

    assert fido.tricks == ['roll over']
    assert buddy.tricks == ['play dead']
