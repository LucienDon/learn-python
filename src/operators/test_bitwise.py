"""位运算符

@see: https://www.w3schools.com/python/python_operators.asp

位运算符在位级上操作数字。
"""


def test_bitwise_operators():
    """位运算符"""

    # 与运算
    # 同位都为1，则取1，否则为0.
    #
    # Example:
    # 5 = 0b0101
    # 3 = 0b0011
    assert 5 & 3 == 1  # 0b0001

    # 或运算
    # 如果两个位中有一个为1，则设置每个位为1。
    #
    # Example:
    # 5 = 0b0101
    # 3 = 0b0011
    assert 5 | 3 == 7  # 0b0111

    # 非运算
    # 反转所有位。
    assert ~5 == -6

    # 异或运算
    # 当两个位中只有一个为1时，将每个位设为1。
    #
    # Example:·
    # 5 = 0b0101
    # 3 = 0b0011
    number = 5  # 0b0101
    number ^= 3  # 0b0011
    assert 5 ^ 3 == 6  # 0b0110

    # 右移运算
    # 通过将最左边位的副本从左边推入，向右移动，并让最右边位位脱落。
    #
    # Example:
    # 5 = 0b0101
    assert 5 >> 1 == 2  # 0b0010
    assert 5 >> 2 == 1  # 0b0001

    # 左移0填充
    # 从右往左推0，让最左边的位去掉。
    #
    # Example:
    # 5 = 0b0101
    assert 5 << 1 == 10  # 0b1010
    assert 5 << 2 == 20  # 0b10100
