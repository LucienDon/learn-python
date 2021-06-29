"""类定义的语法.

@see: https://docs.python.org/3/tutorial/classes.html#class-objects

定义了类的类属性后，可以通过将对象赋值给变量来创建类对象。创建的对象将具有与其关联的实例属性。
"""


def test_class_objects():
    """类对象。

    类对象支持两种操作:
    - 属性引用
    - 实例化
    """

    # 属性引用使用Python中用于所有属性引用的标准语法: obj.name.
    # 有效的属性名是创建类对象时类的命名空间中的所有名称。
    # 对于MyCounter类，以下引用是有效的属性引用:

    class ComplexNumber:
        """复数类的例子"""

        real = 0
        imaginary = 0

        def get_real(self):
            """返回复数的实部。"""
            return self.real

        def get_imaginary(self):
            """返回复数的虚部。"""
            return self.imaginary

    assert ComplexNumber.real == 0

    # __doc__ 也是一个有效的属性，返回属于类的文档字符串
    assert ComplexNumber.__doc__ == '复数类的例子'

    # 类属性也可以被赋值，因此可以更改 ComplexNumber 的值。计数器的任务。
    ComplexNumber.real = 10
    assert ComplexNumber.real == 10

    # 类实例化使用函数表示法。只需假设类对象是一个返回类的新实例的无参数函数。例如(假设上面的类):
    complex_number = ComplexNumber()

    assert complex_number.real == 10
    assert complex_number.get_real() == 10

    # 让我们把计数器的默认值改回来。
    ComplexNumber.real = 10
    assert ComplexNumber.real == 10

    # 实例化操作(“调用”类对象)创建一个空对象。许多类喜欢创建具有自定义到特定初始状态的实例的对象。
    # 因此，类可以定义一个名为__init__()的特殊方法，像这样:

    class ComplexNumberWithConstructor:
        """带有构造函数的类示例"""

        def __init__(self, real_part, imaginary_part):
            self.real = real_part
            self.imaginary = imaginary_part

        def get_real(self):
            """Return real part of complex number."""
            return self.real

        def get_imaginary(self):
            """Return imaginary part of complex number."""
            return self.imaginary

    complex_number = ComplexNumberWithConstructor(3.0, -4.5)
    assert complex_number.real, complex_number.imaginary == (3.0, -4.5)
