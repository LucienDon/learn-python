"""多重继承

@see: https://docs.python.org/3/tutorial/classes.html#multiple-inheritance

有些类可能派生多个类。 这意味着派生类将具有自己的属性，以及派生它的所有类的属性。
"""


def test_multiple_inheritance():
    """多重继承"""

    # pylint: disable=too-few-public-methods
    class Clock:
        """Clock 类"""

        time = '11:23 PM'

        def get_time(self):
            """获取当前时间

            方法是硬编码的，只是为了演示多重继承。
            """
            return self.time

    # pylint: disable=too-few-public-methods
    class Calendar:
        """Calendar class"""

        date = '12/08/2018'

        def get_date(self):
            """获得当前日期

           方法是硬编码的，只是为了演示多重继承。
            """
            return self.date

    # Python还支持一种形式的多重继承。包含多个的类定义
    # base classes looks like this.
    class CalendarClock(Clock, Calendar):
        """使用多重继承的类。

        在大多数情况下，在最简单的情况下，可以将从父类继承的属性的搜索视为深度优先，从左到右，而不是在层次结构中有重叠的同一个类中搜索两次。
        因此，如果在CalendarClock中没有找到某个属性，就在Clock中搜索它，然后(递归地)在Clock的基类中搜索它，
        如果在那里没有找到，就在Calendar中搜索它，依此类推。

        事实上，实际情况要稍微复杂一些;方法解析顺序会动态更改，以支持对 super() 的协作调用。
        这种方法在其他一些多继承语言中称为“调用下一个方法”(call-next-method)，
        比单继承语言中的超级调用更强大。

        动态排序是必要的，因为所有多重继承的情况都显示出一个或多个菱形关系(其中至少有一个父类可以从最底的类通过多个路径访问)。
        例如，所有的类都继承自object，因此任何多重继承的情况都提供了多个到达object的路径。
        保持不止一次被访问的基类,动态算法线性搜索顺序的方式保存每个类中指定的从左到右的顺序,每个父母只有一次调用,这是单调(也就是说,一个类可以派生子类而不影响其父母)的优先顺序。
        """

    calendar_clock = CalendarClock()

    assert calendar_clock.get_date() == '12/08/2018'
    assert calendar_clock.get_time() == '11:23 PM'
