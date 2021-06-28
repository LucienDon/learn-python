# Python语法

**与其他编程语言相比的Python语法**

- Python是为可读性而设计的，受数学影响，和英语有一些相似之处。
- Python使用新行来完成命令，而其他编程语言通常使用分号或括号。
- Python依赖缩进，使用空格来定义作用域;如循环、函数和类的作用域。其他编程语言经常为此使用大括号。
## Python 缩进

在其他编程语言中，代码的缩进只是为了可读性，而在Python中缩进是非常重要的。

Python使用缩进来表示代码块。
```python
if 5 > 2:
  print("Five is greater than two!")
```

如果你跳过缩进，Python会给你一个错误。

## 注释

Python具有注释功能，用于代码内文档。

注释以' '开头，Python会将该行的其余部分呈现为注释:
```python
#This is a comment.
print("Hello, World!")
```

## 文档注释

Python还具有扩展的文档功能，称为文档字符串。

文档字符串可以是一行或多行。文档字符串也是注释:

Python在文档字符串的开头和结尾使用了三引号:
```python
"""This is a 
multiline docstring."""
print("Hello, World!")
```

## 参考

- [w3schools.com](https://www.w3schools.com/python/python_syntax.asp)
