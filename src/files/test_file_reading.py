"""读写文件

@see: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

读取和写入文件的过程就像找到一本书然后打开一本书。
首先，定位文件，打开到第一页，然后读写开始，直到到达文件的末尾。
"""


def test_files_open():
    """打开文件

    open() 返回一个文件对象，最常用的是带两个参数: open (filename, mode)。

    第一个参数是一个包含文件名的字符串。
    第二个参数是另一个字符串，其中包含一些描述文件使用方式的字符。
    模式可以是:

    - 'r' 当文件只被读取时,
    - 'w' 对于仅写(将删除同名的现有文件)，
    - 'a' 打开附加文件;写入文件的任何数据都会自动添加到文件末尾。
    - 'r+' 打开文件进行读写。

    mode 参数是可选的; 如果省略，将假定为'r'。

    通常，文件以文本模式打开，这意味着您从文件中读取和写入字符串，这些字符串以特定的编码方式编码。
    如果没有指定编码，默认值是平台相关的(参见open())。
    附加到 mode的'b'以二进制模式打开文件:现在数据以字节对象的形式读取和写入。
    这种模式应该用于所有不包含文本的文件。

    在文本模式下，读取时的默认值是将平台特定的行结束符(在Unix上是\n，在Windows上是\r\n)转换为仅\n。
    当以文本模式写入时，默认是将出现的\n转换回特定于平台的行结束符。这种对文件数据的幕后修改对于文本文件来说没问题，
    但是会破坏JPEG或EXE文件中的二进制数据。在读写这类文件时，要非常小心地使用二进制模式。

    在处理文件对象时，最好使用with关键字。这样做的好处是，即使在某个时刻引发了异常，文件在套件结束后也会被正确地关闭。
    与写等效的try-finally块相比，Using with 要短得多:
    """

    # 不使用'with'语句打开文件。
    file = open('multi_line_file.txt', 'r')

    assert not file.closed

    read_data = file.read()

    assert read_data == (
        'first line\n'
        'second line\n'
        'third line'
    )

    file.close()

    assert file.closed

    # 使用with打开文件。
    with open('multi_line_file.txt', 'r') as file:
        read_data = file.read()

        assert read_data == (
            'first line\n'
            'second line\n'
            'third line'
        )

    assert file.closed

    # 如果你不使用 with 关键字，那么你应该调用f.close()关闭文件， 并立即释放它使用的任何系统资源。如果你不显式地关闭一个文件，
    # Python 的垃圾收集器将最终销毁该对象并为你关闭打开的文件，但该文件可能会保持打开一段时间。
    # 另一个风险是，不同的Python实现将在不同的时间进行这种清理。
