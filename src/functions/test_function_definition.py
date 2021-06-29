"""函数定义

@see: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
@see: https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

关键字def引入了一个函数定义。
它后面必须有函数名和带括号的形式参数列表。
构成函数体的语句从下一行开始，必须缩进。
"""


def fibonacci_function_example(number_limit):
    """生成最多为 number_limit的 Fibonacci 序列。

    函数体的第一个语句可以是一个字符串字面值;
    这个字符串字面值是函数的文档字符串，或docstring。
    有些工具使用文档字符串自动生成在线或打印文档，或让用户交互式地浏览代码;
    在编写的代码中包含文档字符串是一种很好的做法，因此要养成这种习惯。
    """

    # 函数的执行引入了一个新的符号表，用于函数的局部变量。
    # 更准确地说，函数中所有的变量赋值都存储在局部符号表中;
    # 而变量引用首先在局部符号表中查找，然后在外围函数的局部符号表中查找，然后在全局符号表中查找，最后在内置名称表中查找。
    # 因此，全局变量不能在函数中直接赋值(除非在global语句中命名)，尽管它们可以被引用。
    fibonacci_list = []
    previous_number, current_number = 0, 1
    while previous_number < number_limit:
        # 语句 result.append(a)调用列表对象 result 的一个方法。
        # 方法是一个“属于”一个对象的函数，命名为obj。Methodname，其中obj是某个对象(这可能是一个表达式)，方法名是由对象类型定义的方法的名称。
        # 不同的类型定义不同的方法。
        # 不同类型的方法可以具有相同的名称而不会造成歧义。 (可以使用类定义自己的对象类型和方法, see Classes)
        # 示例中所示的 append() 方法是为列表对象定义的;
        # 它在列表的末尾添加一个新元素。在这个例子中，它相当于result = result + [a]，但是效率更高。
        fibonacci_list.append(previous_number)
        # 这是一个多重赋值语句。
        previous_number, current_number = current_number, previous_number + current_number

    # return 语句从函数中返回一个值。
    # 不带表达式参数的 return 返回 None。如果函数结束也返回 None。
    return fibonacci_list


def test_function_definition():
    """函数定义"""

    # 现在调用我们刚刚定义的函数。
    assert fibonacci_function_example(300) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

    # 函数定义在当前符号表中引入函数名。
    # 函数名的值具有解释器识别为用户定义函数的类型。
    # 这个值可以分配给另一个名称，然后也可以作为函数使用。
    # 这是一种通用的重命名机制
    fibonacci_function_clone = fibonacci_function_example
    assert fibonacci_function_clone(300) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

    # 在 Python 中，函数是第一类公民，它们是对象，这意味着我们可以用它们做很多有用的事情。

    # 为变量分配函数。

    def greet(name):
        return 'Hello, ' + name

    greet_someone = greet

    assert greet_someone('John') == 'Hello, John'

    # 在其他函数中定义函数。

    def greet_again(name):
        def get_message():
            return 'Hello, '

        result = get_message() + name
        return result

    assert greet_again('John') == 'Hello, John'

    # 函数可以作为参数传递给其他函数。

    def greet_one_more(name):
        return 'Hello, ' + name

    def call_func(func):
        other_name = 'John'
        return func(other_name)

    assert call_func(greet_one_more) == 'Hello, John'

    # 函数可以返回其他函数。换句话说，函数生成其他函数。

    def compose_greet_func():
        def get_message():
            return 'Hello there!'

        return get_message

    greet_function = compose_greet_func()
    assert greet_function() == 'Hello there!'

    # 内部函数可以访问外围作用域。

    # 更常见的说法是结束。
    # 这是一个非常强大的模式
    # 另外需要注意的是，Python 只允许对外部作用域的读访问，而不允许赋值。
    # 注意，我们是如何修改上面的示例，从内部函数的封闭作用域读取“name”参数并返回新函数的。

    def compose_greet_func_with_closure(name):
        def get_message():
            return 'Hello there, ' + name + '!'

        return get_message

    greet_with_closure = compose_greet_func_with_closure('John')

    assert greet_with_closure() == 'Hello there, John!'
