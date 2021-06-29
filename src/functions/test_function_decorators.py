"""函数修饰符。

@see: https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

函数装饰器只是现有函数的包装器。
在设计模式的上下文中，装饰器动态地改变函数、方法或类的功能，而不必直接使用子类。
当您需要扩展不想修改的函数的功能时，这是理想的。
我们可以在任何地方实现装饰器模式，但 Python 通过提供更具表达性的特性和语法来促进实现。
"""


def test_function_decorators():
    """函数修饰符。"""

    # 函数装饰器只是现有函数的包装器。把上面提到的想法放在一起，我们就可以建立一个装饰。
    # 在本例中，让我们考虑一个函数，它通过 p 标记包装另一个函数的字符串输出。

    # 这就是我们想要装饰的功能。
    def greeting(name):
        return "Hello, {0}!".format(name)

    # 这个函数用 <p> 标记修饰了另一个函数的输出。
    def decorate_with_p(func):
        def function_wrapper(name):
            return "<p>{0}</p>".format(func(name))

        return function_wrapper

    # 现在，让我们调用装饰器，并将我们想要装饰的函数传递给它。
    my_get_text = decorate_with_p(greeting)

    # 开始吧，我们只是修饰了函数的输出，而没有改变函数本身。
    # 执行过程：
    # my_get_text('John')
    # -> decorate_with_p(greeting('John'))
    # -> function_wrapper('John')
    # -> "<p>{0}</p>".format(greeting('John'))
    # -> "<p>{0}</p>".format("Hello, {0}!".format('John'))
    # -> '<p>Hello, John!</p>'

    assert my_get_text('John') == '<p>Hello, John!</p>'  # With decorator.
    assert greeting('John') == 'Hello, John!'  # Without decorator.

    # 现在，Python通过一些语法上的“糖果”让程序员创建和使用装饰器变得更干净、更好。
    # 对此，有一个简洁的快捷方式，就是在要装饰的函数之前提到装饰函数的名称。
    # 装饰器的名称应该以@符号作为前缀。

    @decorate_with_p
    def greeting_with_p(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_p('John') == '<p>Hello, John!</p>'

    # 现在，让我们考虑一下，我们想要通过多一个函数来装饰我们的greeting函数，以包装字符串输出的div。

    # 这是我们的第二个装饰器。
    def decorate_with_div(func):
        def function_wrapper(text):
            return "<div>{0}</div>".format(func(text))
        return function_wrapper

    # 对于基本方法，装饰 get_text 将沿着 greeting_with_div_p = decorate_with_div(decorate_with_p(greeting_with_p)) 的思路进行

    # 使用Python的装饰器语法，同样的事情可以以更强大的表达能力实现。
    @decorate_with_div
    @decorate_with_p
    def greeting_with_div_p(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_div_p('John') == '<div><p>Hello, John!</p></div>'

    # 这里需要注意的重要一点是，设置装饰器的顺序很重要。
    # 如果上面例子中的顺序不同，输出就会不同。

    # 向装饰器传递参数。

    # 回顾前面的示例，您可以注意到示例中的装饰器有多冗余。
    # 2个装饰器(decorate_with_div, decorate_with_p)都具有相同的功能，但使用不同的标签包装字符串。
    # 我们绝对可以做得更好。 为什么不提供一个更通用的实现，将标签作为字符串进行包装呢?
    # 是的,请!

    def tags(tag_name):
        def tags_decorator(func):
            def func_wrapper(name):
                return "<{0}>{1}</{0}>".format(tag_name, func(name))

            return func_wrapper

        return tags_decorator

    @tags('div')
    @tags('p')
    def greeting_with_tags(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_tags('John') == '<div><p>Hello, John!</p></div>'
