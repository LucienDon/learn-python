"""包.

@see: https://docs.python.org/3/tutorial/modules.html#packages

包是一种通过使用“带点的模块名称”来构造Python模块名称空间的方法。
例如，模块名A.B在名为A的包中指定了名为B的子模块。
就像使用模块可以让不同模块的作者不必担心彼此的全局变量名一样，使用带点的模块名可以让多模块包(如NumPy或Pillow)的作者不必担心彼此的模块名。

需要__init__.py文件才能使 Python 将这些目录视为包含包; 这样做是为了防止具有公共名称(如字符串)的目录无意中隐藏了稍后在模块搜索路径上出现的有效模块。
在最简单的情况下，__init__.py可以只是一个空文件，但它也可以为包执行初始化代码或设置__all__变量，稍后将进行描述。

当解释器执行import语句时，它会在从以下来源组装的目录列表中搜索module:

- 在其中运行输入脚本的目录，如果解释器正在交互式地运行，则为当前目录
- PYTHONPATH环境变量中包含的目录列表(如果设置了的话)。(PYTHONPATH的格式依赖于操作系统，但应该模仿PATH环境变量。)
- 安装Python时配置的与安装相关的目录列表

得到的搜索路径可以在Python变量sys.path中访问。路径，该路径从名为sys的模块中获取。

>>> import sys
>>> sys.path

@see: https://realpython.com/python-modules-packages/
"""

# 例如，包的用户可以从包中导入单个模块。
import sound_package.effects.echo

# 另一种导入子模块的方法是:

# pylint: disable=reimported
from sound_package.effects import echo

# 还有一种方法是直接导入需要的函数或变量:
from sound_package.effects.echo import echo_function


# 请注意，当使用from package import item时，item可以是包的子模块(或子包)，也可以是包中定义的其他名称，如函数、类或变量。
# import语句首先测试项是否在包中定义;如果不是，则假定它是一个模块并尝试加载它。
# 如果没有找到，就会引发ImportError异常。

# 相反，当使用类似import item.subitem的语法时。分子项，除最后一项外，每一项必须是一个包裹;
# 最后一项可以是模块或包，但不能是前一项中定义的类、函数或变量。


def test_packages():
    """Packages."""
    assert sound_package.effects.echo.echo_function() == 'Do echo effect'
    assert echo.echo_function() == 'Do echo effect'
    assert echo_function() == 'Do echo effect'
