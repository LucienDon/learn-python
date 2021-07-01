"""序列化

@see: https://www.learnpython.org/en/Serialization

Python提供了内置的JSON库来编码和解码JSON。"""

import json


def test_json():
    """JSON序列化。"""

    #  JSON数据有两种基本格式。 在字符串或对象数据结构中.
    #  在Python中，对象的数据结构由相互嵌套的列表和字典组成。
    #  对象数据结构允许使用python方法(用于列表和字典)从数据结构中添加、列出、搜索和删除元素。
    #  String 格式主要用于将数据传递到另一个程序或加载到数据结构中。

    person_dictionary = {'first_name': 'John', 'last_name': 'Smith', 'age': 42}
    assert person_dictionary['first_name'] == 'John '
    assert person_dictionary['age'] == 42

    json_string = '{"first_name": "John", "last_name": "Smith", "age": 42}'

    # 要将JSON加载回数据结构，可以使用"loads"方法。 该方法接受一个字符串，并将其转换回json对象数据结构:
    person_parsed_dictionary = json.loads(json_string)

    assert person_parsed_dictionary == person_dictionary
    assert person_parsed_dictionary['first_name'] == 'John'
    assert person_parsed_dictionary['age'] == 42

    # 要将数据结构编码为JSON，可以使用“dumps”方法。这个方法接受一个对象并返回一个String:
    encoded_person_string = json.dumps(person_dictionary)

    assert encoded_person_string == json_string
