"""类定义的语法。

@see: https://docs.python.org/3/tutorial/classes.html#instance-objects
"""


def test_instance_objects():
    """实例对象。

    现在我们可以用实例对象做什么?实例对象唯一能理解的操作是属性引用。有效的属性名有两种:
    - 数据属性
    - 方法
    """

    # 数据属性不需要声明;像局部变量一样，它们在第一次被赋值时就会出现。
    # 例如，如果x是上面创建的MyCounter的实例，下面的代码段将打印值16，而不留下跟踪。

    # pylint: disable=too-few-public-methods
    class DummyClass:
        """伪类"""
        pass

    dummy_instance = DummyClass()

    # pylint: disable=attribute-defined-outside-init
    dummy_instance.temporary_attribute = 1
    assert dummy_instance.temporary_attribute == 1
    del dummy_instance.temporary_attribute
