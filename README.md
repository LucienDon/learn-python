# Python 学习笔记

[![Build Status](https://travis-ci.org/trekhleb/learn-python.svg?branch=master)](https://travis-ci.org/trekhleb/learn-python)

> 这是 Python 脚本的集合，按 [目录](#目录)划分，包含带有解释的代码示例、不同的用例和进一步阅读的链接。


这是一个**练习场**，因为您可以更改或添加代码以查看它是如何工作的，
并使用断言 [测试代码](#测试代码)。它还允许您 [代码检测](#代码检测) 
并检查它是否符合 Python 代码风格指南。
总而言之，它可能会使您的学习过程更具交互性，并且可能会帮助您从一开始就保持较高的代码质量。

这是一个**备忘单**，因为一旦您想回顾[标准 Python 语句和结构](#目录)的语法，您可能会回到这些代码示例。
此外，由于代码中充满了断言，您无需启动它们就可以立即看到预期的函数语句输出。

> _你可能也对🤖感兴趣 [交互式机器学习实验](https://github.com/trekhleb/machine-learning-experiments)_

## 如何使用此存储库

此存储库中的每个 Python 脚本都具有以下结构：

```python
"""Lists  <--- 这里的主题名称

# @see: https://www.learnpython.org/en/Lists  <-- 进一步阅读的链接在这里

这里可能会对当前主题进行更详细的解释（即关于列表的一般信息）。
"""


def test_list_type():
    """
        子主题的解释在这里。每个文件都包含说明子主题的测试函数（即列表类型、列表方法）。
    """
    
    # 以下是如何构建列表的示例。 <-- 这里的评论解释了这个动作
    squares = [1, 4, 9, 16, 25]
    
    # 列表可以被索引和切片。
    # 索引返回项目。
    assert squares[0] == 1  # <-- 这里的断言说明了结果。
    # 切片返回一个新列表。
    assert squares[-3:] == [9, 16, 25]  # <-- 这里的断言说明了结果。
```

所以通常你可能想要执行以下操作：

- [Find the topic](#table-of-contents)你想学习或回顾。
- 阅读每个脚本的文档字符串中链接的注释和/或文档（如上例所示）。
- 查看代码示例和断言以查看使用示例和预期输出。
- 更改代码或添加新断言以查看工作方式。
- [Run tests](#testing-the-code) and [lint the code](#linting-the-code) 看看它是否有效并且是否正确写入。

## 目录

1. **入门**
    - [什么是 Python](src/getting_started/what_is_python.md)
    - [Python 语法](src/getting_started/python_syntax.md)
    - [变量](src/getting_started/test_variables.py)
2. **运算符**
    - [算术运算符](src/operators/test_arithmetic.py) (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
    - [位运算符](src/operators/test_bitwise.py) (`&`, `|`, `^`, `>>`, `<<`, `~`)
    - [赋值运算符](src/operators/test_assigment.py) (`=`, `+=`, `-=`, `/=`, `//=` etc.)
    - [比较运算符](src/operators/test_comparison.py) (`==`, `!=`, `>`, `<`, `>=`, `<=`)
    - [逻辑运算符](src/operators/test_logical.py) (`and`, `or`, `not`)
    - [恒等运算符](src/operators/test_identity.py) (`is`, `is not`)
    - [成员运算符](src/operators/test_membership.py) (`in`, `not in`)
3. **数据类型**
    - [数字](src/data_types/test_numbers.py) (其中包括布尔值)
    - [字符串](src/data_types/test_strings.py) 以及方法
    - [列表](src/data_types/test_lists.py) 以及方法(包括列表推导式)
    - [元组](src/data_types/test_tuples.py)
    - [集合](src/data_types/test_sets.py)及其方法
    - [字典](src/data_types/test_dictionaries.py)
    - [Type Casting](src/data_types/test_type_casting.py)
4. **控制**
    - [if](src/control_flow/test_if.py)
    - [for](src/control_flow/test_for.py) (以及 `range()` 函数)
    - [while](src/control_flow/test_while.py)
    - [try](src/control_flow/test_try.py)
    - [break](src/control_flow/test_break.py)
    - [continue](src/control_flow/test_continue.py)
5. **函数**
    - [函数定义](src/functions/test_function_definition.py) (`def` and `return` statements)
    - [函数内部变量的作用域](src/functions/test_function_scopes.py) (`global` and `nonlocal` statements)
    - [默认参数值](src/functions/test_function_default_arguments.py)
    - [关键字参数](src/functions/test_function_keyword_arguments.py)
    - [任意的参数列表](src/functions/test_function_arbitrary_arguments.py)
    - [拆包参数列表](src/functions/test_function_unpacking_arguments.py) (`*` and `**` statements)
    - [Lambda表达式](src/functions/test_lambda_expressions.py) (`lambda` statement)
    - [文档字符串](src/functions/test_function_documentation_string.py)
    - [函数注释](src/functions/test_function_annotations.py)
    - [函数修饰符](src/functions/test_function_decorators.py)
6. **类**
    - [类定义](src/classes/test_class_definition.py) (`class` statement)
    - [类对象](src/classes/test_class_objects.py)
    - [实例对象](src/classes/test_instance_objects.py)
    - [方法对象](src/classes/test_method_objects.py)
    - [类和实例变量](src/classes/test_class_and_instance_variables.py)
    - [继承](src/classes/test_inheritance.py)
    - [多重继承](src/classes/test_multiple_inheritance.py)
7. **组件**
    - [组件](src/modules/test_modules.py) (`import` statement)
    - [包](src/modules/test_packages.py)
8. **错误和异常**
    - [处理异常](src/exceptions/test_handle_exceptions.py) (`try` statement)
    - [提高异常](src/exceptions/test_raise_exceptions.py) (`raise` statement) 
9. **文件**
    - [读与写](src/files/test_file_reading.py) (`with` statement)
    - [文件对象的方法](src/files/test_file_methods.py)
10. **附加物**
    - [`pass` 声明](src/additions/test_pass.py)
    - [生成器](src/additions/test_generators.py) (`yield` 声明)
11. **标准库简介**
    - [序列化](src/standard_libraries/test_json.py) (`json` library)
    - [文件通配符](src/standard_libraries/test_glob.py) (`glob` library)
    - [字符串匹配](src/standard_libraries/test_re.py) (`re` library)
    - [数学运算](src/standard_libraries/test_math.py) (`math`, `random`, `statistics` libraries)
    - [日期和时间](src/standard_libraries/test_datetime.py) (`datetime` library)
    - [数据压缩](src/standard_libraries/test_zlib.py) (`zlib` library)

## 预备知识

**安装Python**

确保你安装了[Python3](https://realpython.com/installing-python/) on your machine.

你可能想要使用[venv](https://docs.python.org/3/library/venv.html)标准Python库
创建虚拟环境并安装Python、pip和所有依赖包从本地项目目录提供，以避免与系统范围的包及其版本。

根据你的安装，你可以通过运行`python` 或 `python3`。pip包管理器也是如此——它也可能是可访问的
通过运行 `pip `或` pip3 `。

You may check your Python version by running:

```bash
python --version
```

Note that in this repository whenever you see `python` it will be assumed that it is Python **3**.

**Installing dependencies**

Install all dependencies that are required for the project by running:

```bash
pip install -r requirements.txt
```

## 测试代码

测试使用 [pytest](https://docs.pytest.org/en/latest/) 框架.

您可以通过 `test_` 作为前缀添加文件和函数为自己添加新的测试 
(例如： 在 `test_topic.py` 里添加  `def test_sub_topic()` 函数).

要运行所有测试，请从项目根文件夹执行以下命令:

```bash
pytest
```

要运行特定的测试，请执行:

```bash
pytest ./path/to/the/test_file.py
```

## 代码检测

代码检测用的是 [pylint](http://pylint.pycqa.org/) 和 [flake8](http://flake8.pycqa.org/en/latest/) 库.

### PyLint

来检查代码是否按 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 规定编写,请执行:

```bash
pylint ./src/
```

以防linter检测到错误 (i.e. `missing-docstring`) 你可能想读更多关于
具体运行错误:

```bash
pylint --help-msg=missing-docstring
```

[More about PyLint](http://pylint.pycqa.org/)

### Flake8

来检查代码是否按 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 规定编写,请执行:

```bash
flake8 ./src
```

或者，如果你想有更详细的输出，你可以运行:

```bash
flake8 ./src --statistics --show-source --count
```
