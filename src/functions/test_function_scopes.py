"""作用域和命名空间

@see: https://docs.python.org/3/tutorial/classes.html#scopes-and-namespaces-example

NAMESPACE是从名称到对象的映射。
大多数名称空间目前都以 Python 字典的形式实现，但这通常不会引起注意(除了性能)，将来可能会改变。
命名空间的例子有: 一组内置名称(包含像abs()这样的函数和内置异常名称);
模块中的全局名称; 以及函数调用中的局部名称. 从某种意义上说，对象的一组属性也构成了一个名称空间。
关于名称空间，需要知道的重要一点是，名称之间绝对没有关系在不同的名称空间;
例如，两个不同的模块都可以定义一个 maximize 函数不要混淆——模块的用户必须以模块名作为前缀。

顺便说一下,我们对点后面的任何名称都使用attribute — for example, 在表达式 z.real, real 是对象 z 的属性.
严格地说,在模块中对名称的引用是属性引用: 在表达式 modname.func_name, modname 是一个模块对象并且 func_name
是它的一个属性. 在这种情况下 ,碰巧有一个直接的映射模块的属性和模块中定义的全局名称: 它们共享相同的命名空间!

SCOPE 是 Python程序的文本区域，其中名称空间可以直接访问。
这里的“直接可访问” 意味着对名称的非限定引用试图找到该名称在名称空间中。

虽然作用域是静态确定的，但它们是动态使用的。 在执行期间的任何时候，至少有三个可直接访问其名称空间的嵌套作用域:
- 首先搜索的最内层作用域包含本地名称。
- 任何封闭函数的作用域(从最近的封闭作用域开始搜索)都包含非局部名称，但也包含非全局名称。
- 倒数第二个作用域包含当前模块的全局名称。
- 最外层作用域(最后搜索)是包含内置名称的命名空间。

小心! !
-------------
从内部函数中更改全局或非局部变量可能是一个糟糕的实践，可能导致更难调试和更脆弱的代码!只有在你知道自己在做什么的情况下才能这么做。
"""

# pylint: disable=invalid-name
test_variable = 'initial global value'


def test_function_scopes():
    """作用域和命名空间示例"""

    # 这个示例演示了如何引用不同的作用域和名称空间，以及全局和非局部如何影响变量绑定:

    # pylint: disable=redefined-outer-name
    test_variable = 'initial value inside test function'

    def do_local():
        # 创建只能在当前 do_local() 函数中访问的变量。
        # pylint: disable=redefined-outer-name
        test_variable = 'local value'
        return test_variable

    def do_nonlocal():
        # 从外部范围处理变量并尝试改变它。
        # pylint: disable=redefined-outer-name
        nonlocal test_variable
        test_variable = 'nonlocal value'
        return test_variable

    def do_global():
        # 从非常全局的范围处理变量并尝试改变它。
        # pylint: disable=redefined-outer-name,global-statement
        global test_variable
        test_variable = 'global value'
        return test_variable

    # 在这个级别上，我们可以访问test_function_scopes()函数变量的local。
    assert test_variable == 'initial value inside test function'

    # Do local assignment.
    # 它不改变全局变量和 test_function_scopes() 作用域的变量。
    do_local()
    assert test_variable == 'initial value inside test function'

    # Do non local assignment.
    # 它不改变全局变量，但它从 test_function_scopes() 函数范围改变变量。
    do_nonlocal()
    assert test_variable == 'nonlocal value'

    # Do global assignment.
    # 这一个改变全局变量，但不改变变量从 test_function_scopes() 函数范围。
    do_global()
    assert test_variable == 'nonlocal value'


def test_global_variable_access():
    """在函数内部测试全局变量访问"""

    # test_variable 的全局值已经在之前的测试中被 do_global() 函数改变了，所以让我们检查一下。
    # pylint: disable=global-statement
    global test_variable
    assert test_variable == 'global value'

    # 在这个示例中，您可以看到从内部函数中访问和更改全局变量可能会使调试更加困难，代码也更难以预测。
    # 因为你可能期望 test_variable 仍然等于'初始全局值'，但它被 "someone" 改变了，你需要知道谁改变了它的 CONTEXT。
    # 所以只有在你知道自己在做什么的时候才能访问全局和非局部作用域否则这可能会被认为是不好的做法。
