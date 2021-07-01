"""字符串的匹配。

@see: https://docs.python.org/3/tutorial/stdlib.html#string-pattern-matching

re模块提供了用于高级字符串处理的正则表达式工具。
对于复杂的匹配和操作，正则表达式提供了简洁、优化的解决方案:
"""

import re


def test_re():
    """String Pattern Matching"""

    assert re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest') == [
        'foot',
        'fell',
        'fastest'
    ]

    assert re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat') == 'cat in the hat'

    # 当只需要简单的功能时，字符串方法是首选的，因为它们更容易阅读和调试:
    assert 'tea for too'.replace('too', 'two') == 'tea for two'
