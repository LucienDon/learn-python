"""模块.

@see: https://docs.python.org/3/tutorial/modules.html

随着程序变得越来越长，您可能希望将它分成几个文件，以便于维护。
您可能还希望使用在多个程序中编写的方便函数，而不需要将其定义复制到每个程序中。

为了支持这一点，Python有一种方法将定义放在文件中，并在脚本或解释器的交互式实例中使用它们。
这样的文件称为模块; 来自模块的定义可以导入到其他模块或主模块中 (在顶层和计算器模式下执行的脚本中可以访问的变量集合)。

模块是包含Python定义和语句的文件。 文件名是带有.py后缀的模块名。在一个模块中，模块名(作为字符串)可以作为全局变量__name__的值。

当解释器执行import语句时，它会在从以下来源组装的目录列表中搜索module:

- 在其中运行输入脚本的目录，如果解释器正在交互式地运行，则为当前目录
- PYTHONPATH 环境变量中包含的目录列表 (如果设置了的话)。 (PYTHONPATH的格式依赖于操作系统，但应该模仿PATH环境变量。)
- 安装Python时配置的与安装相关的目录列表

可以在 Python 变量 sys.path 中得到的搜索路径，该路径从 sys 的模块中获取:

#>>> import sys
#>>> sys.path

@see: https://realpython.com/python-modules-packages/
"""

# 这不会在当前符号表中直接输入fibonacci_module中定义的函数名;它只在那里输入模块名fibonacci_module。
import fibonacci_module
# 如果模块名后面跟着 as，那么 as 后面的名称直接绑定到导入的模块:
import fibonacci_module as fibonacci_module_renamed
# pylint: disable=reimported
from fibonacci_module import fibonacci_at_position, fibonacci_smaller_than
# 当使用 from 时也可以使用，效果类似:
from fibonacci_module import fibonacci_at_position as fibonacci_at_position_renamed


# import 语句有一个变体，它可以直接将模块中的名称导入到导入模块的符号表中。 例如:
# 甚至还有一个变量可以导入模块定义的所有名称。 这将导入除下划线(_)开头的所有名称。
# 在大多数情况下，Python程序员不使用这个功能，因为它将一组未知的名称引入解释器，可能隐藏了您已经定义的一些内容。
# >>> from fibonacci_module import *


# 当一个名为 spam 的模块被导入时，解释器首先搜索具有该名称的内置模块。
# 如果没有找到，它就搜索一个名为 spam 的文件。
# 由变量 sys.path 给出的目录列表中的 py。
# sys.path 是从这些位置初始化的:
#
# - 包含输入脚本的目录(或未指定文件时的当前目录)。
# - PYTHONPATH(目录名列表，语法与 shell 变量 PATH 相同)。
# - installation-dependent 默认。


def test_modules():
    """Modules"""

    assert fibonacci_module.fibonacci_at_position(7) == 13
    assert fibonacci_at_position(7) == 13
    assert fibonacci_module_renamed.fibonacci_at_position(7) == 13
    assert fibonacci_at_position_renamed(7) == 13

    assert fibonacci_module.fibonacci_smaller_than(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert fibonacci_smaller_than(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert fibonacci_module_renamed.fibonacci_smaller_than(10) == [0, 1, 1, 2, 3, 5, 8]

    # 如果你想经常使用一个函数，你可以把它赋给一个本地名称。
    fibonacci = fibonacci_module.fibonacci_smaller_than
    assert fibonacci(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # 内置函数dir()用于找出一个模块定义了哪些名称。它返回一个已排序的字符串列表。
    assert dir(fibonacci_module) == [
        '__builtins__',
        '__cached__',
        '__doc__',
        '__file__',
        '__loader__',
        '__name__',
        '__package__',
        '__spec__',
        'fibonacci_at_position',
        'fibonacci_smaller_than',
    ]
