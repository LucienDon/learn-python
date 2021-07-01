"""File Wildcards.

@see: https://docs.python.org/3/tutorial/stdlib.html#file-wildcards

glob 模块提供了一个通过目录通配符搜索生成文件列表的函数:
"""

import glob


def test_glob():
    """File Wildcards."""

    # == 操作符依赖于列表中元素的顺序。
    # 在某些情况下(如Linux Mint, python3.6)， glob()函数返回列表的顺序与预期相反。
    # 因此，让我们在比较之前使用sorted()内置函数对两个列表进行排序。
    assert sorted(glob.glob('glob_files/*.txt')) == sorted([
        'glob_files\\first_file.txt',
        'glob_files\\second_file.txt'
    ])
