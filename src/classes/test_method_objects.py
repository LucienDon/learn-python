"""类定义的语法.

@see: https://docs.python.org/3/tutorial/classes.html#method-objects

类可以有两种类型的属性引用:数据或方法。
类方法由[variable_name].[method_name]([parameters])调用，与缺少()的类数据相反。
"""


class MyCounter:
    """计数器类的一个简单示例"""
    counter = 10

    def get_counter(self):
        """Return the counter"""
        return self.counter

    def increment_counter(self):
        """Increment the counter"""
        self.counter += 1
        return self.counter


def test_method_objects():
    """方法对象。"""

    # 另一种实例属性引用是方法。
    # 方法是“属于”对象的函数。
    # (在Python中，方法一词不是类实例所特有的:其他对象类型也可以有方法。
    # 例如，列表对象有append、insert、remove、sort等方法。
    # 但是，在接下来的讨论中，除非另有明确说明，否则我们将使用术语方法专指类实例对象的方法。)

    # 但是要注意 counter。get_counter() 和 mycounter。get_counter()不是一回事 —
    # 它是一个方法对象，不是一个函数对象。

    # 通常，方法在绑定后立即被调用
    counter = MyCounter()
    assert counter.get_counter() == 10

    # 但是，没有必要立即调用一个方法: Counter.get_counter() 是一个方法对象，可以存储起来，以后再调用。
    # 例如:
    get_counter = counter.get_counter
    assert get_counter() == 10

    # 当一个方法被调用时到底发生了什么?
    # 您可能已经注意到，上面调用counter.get_counter()时没有带实参，尽管get_counter()的函数定义指定了一个实参(self)。
    # 参数发生了什么?
    # 当然，当一个需要参数的函数被调用时，Python会引发异常 — 即使这个参数实际上没有被使用……

    # 实际上，您可能已经猜到了答案:方法的特殊之处在于实例对象作为函数的第一个参数传递。
    # 在我们的示例中，调用counter.get_counter() 完全等价于 MyCounter.get_counter(counter).
    # 通常，使用 n个参数列表调用一个方法等同于使用参数列表调用相应的函数，参数列表是通过在第一个参数之前插入方法的实例对象创建的。

    assert counter.get_counter() == 10
    assert MyCounter.get_counter(counter) == 10
