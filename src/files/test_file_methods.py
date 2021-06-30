"""文件对象的方法

@see: https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects

从文件中读取并不总是顺序的。
有一些方法可以查找文件中的特定位置，
就像翻到一本书的某一页一样。
"""


def test_file_methods():
    """文件对象的方法"""

    multi_line_file = open('src/files/multi_line_file.txt', 'r')
    binary_file = open('src/files/binary_file', 'r')

    # 要读取文件的内容，调用f.read(size)，它读取一定量的数据并将其作为字符串(文本模式)或字节对象(二进制模式)返回。
    # size是一个可选的数字参数。
    # 当size被省略或为负值时，将读取并返回文件的全部内容;
    # 如果文件的大小是机器内存的两倍，那就是你的问题了。
    # 否则，最多读取并返回size字节。
    # 如果已经到达文件的末尾，f.read()将返回一个空字符串(").
    read_data = multi_line_file.read()

    # pylint: disable=duplicate-code
    assert read_data == 'first line\nsecond line\nthird line'

    # 要改变文件对象的位置，使用f.s seek(offset, from_what)。
    # 位置从添加offset到参考点计算;参考点由from_what参数选择。
    # from_what值为0表示从文件的开头开始，1使用当前文件位置，2使用文件的结尾作为参考点。
    # From_what可以省略，默认值为0，使用文件的开头作为参考点。
    assert binary_file.seek(0) == 0  # 转到文件的第0个字节
    assert binary_file.seek(6) == 6  # 转到文件中的第6个字节

    assert binary_file.read(1) == '6'

    # readline()从文件中读取一行;
    # 换行符(\n)将留在字符串的末尾，如果文件不以换行符结束，则只在文件的最后一行省略。
    # 这使得返回值没有歧义;如果f.readline()返回一个空字符串，则表示已经到达文件的末尾，
    # 而空行由'\n'表示，这是一个只包含一个换行符的字符串。
    multi_line_file.seek(0)

    assert multi_line_file.readline() == 'first line\n'
    assert multi_line_file.readline() == 'second line\n'
    assert multi_line_file.readline() == 'third line'
    assert multi_line_file.readline() == ''

    multi_line_file.close()
    binary_file.close()
