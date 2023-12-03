"""
datetime 是 Python 中处理日期的标准模块，它提供了 4 种对日期和时间进行处理的类：datetime、date、time 和
timedelta。
"""

"""
1. datetime类
"""
# class datetime(date):
#     def __init__(self, year, month, day, hour, minute, second, microsecond, tzinfo)
#         pass
#     def now(cls, tz=None):
#         pass
#     def timestamp(self):
#         pass
#     def fromtimestamp(cls, t, tz=None):
#         pass
#     def date(self):
#         pass
#     def time(self):
#         pass
#     def year(self):
#         pass
#     def month(self):
#         pass
#     def day(self):
#         pass
#     def hour(self):
#         pass
#     def minute(self):
#         pass
#     def second(self):
#         pass
#     def isoweekday(self):
#         pass
#     def strftime(self, fmt):
#         pass
#     def combine(cls, date, time, tzinfo=True):
#         pass

"""
1. datetime.now(tz=None) 获取当前的日期时间，输出顺序为：年、月、日、时、分、秒、微秒。
2. datetime.timestamp() 获取以 1970年1月1日为起点记录的秒数。
3. datetime.fromtimestamp(tz=None) 使用 unixtimestamp 创建一个 datetime。
"""

# 创建一个datetime对象
import datetime
dt = datetime.datetime(year=2022,month=6,day=12,hour=0,minute=6,second=24)
print(dt) # 2022-06-12 00:06:24
print(dt.timestamp())   # 1654963584.0

dt = datetime.datetime.fromtimestamp(1654963584.0)
print(dt)  # 2022-06-12 00:06:24
print(type(dt))  # <class 'datetime.datetime'>

dt = datetime.datetime.now()
print(dt)   # 2022-06-12 00:24:10.709543
print(type(dt))  # <class 'datetime.datetime'>


"""
datetime.strftime(fmt) 格式化 datetime 对象。
%a 本地简化星期名称（如星期一，返回 Mon）
%A 本地完整星期名称（如星期一，返回 Monday）
%b 本地简化的月份名称（如一月，返回 Jan）
%B 本地完整的月份名称（如一月，返回 January）
%c 本地相应的日期表示和时间表示
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%j 年内的一天（001-366）
%m 月份（01-12）
%M 分钟数（00-59）
%p 本地A.M.或P.M.的等价符
%S 秒（00-59）
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（0000-9999）
%Z 当前时区的名称（如果是本地时间，返回空字符串）
%% %号本身
"""

## 示例 如何将 datetime 对象转换为任何格式的日期？
dt = datetime.datetime(year=2022, month=6,day=12,hour=14,minute=11,second=45)
s = dt.strftime("%Y/%m/%d %H:%M:%S")  # 2022/06/12 14:11:45
print(s)

s = dt.strftime('%d %B, %Y, %A')
print(s)  # 12 June, 2022, Sunday

## 练习： 如何将给定日期转换为 "mmm-dd, YYYY" 的格式？
di = datetime.date(year=2022,month=6,day=12)
print(di.strftime('%b-%d, %Y'))  # Jun-12, 2022

"""
1. datetime.date() Return the date part.
2. datetime.time() Return the time part, with tzinfo None.
3. datetime.year 年
4. datetime.month 月
5. datetime.day 日
6. datetime.hour 小时
7. datetime.minute 分钟
8. datetime.second 秒
9. datetime.isoweekday 星期几
"""

dt = datetime.datetime(year=2022,month=6,day=12,hour=14,minute=22,second=34)
print(dt.date())  # 2022-06-12
print(type(dt.date()))  # <class 'datetime.date'>
print(dt.time())  # 14:22:34
print(type(dt.time()))  # <class 'datetime.time'>
print(dt.year) # 2022
print(dt.month) # 6
print(dt.day) # 12
print(dt.hour) # 14
print(dt.minute) # 22
print(dt.second) # 34
print(dt.isoweekday()) # 7

## 在处理含有字符串日期的数据集或表格时，我们需要一种自动解析字符串的方法，无论它是什么格式的，都可以将其转化为 datetime 对象。这时，就要使用到 dateutil 中的 parser 模块。
## 1. parser.parse(timestr, parserinfo=None, **kwargs)
## 如何在 python 中将字符串解析为 datetime对象？
from dateutil import parser

s = '2022-06-12'
dt = parser.parse(s)
print(dt)  # 2022-06-12 00:00:00
print(type(dt))  # <class 'datetime.datetime'>

s = 'June 12, 2022, 2:31pm'
dt = parser.parse(s)
print(dt)  # 2022-06-12 14:31:00
print(type(dt))  # <class 'datetime.datetime'>

## 练习: 如何将字符串日期解析为 datetime 对象？
s1 = '2022 June 12'
s2 = '12-06-2022'
s3 = 'June12, 2022, 02:35pm'
print(parser.parse(s1)) # 2022-06-12 00:00:00
print(parser.parse(s2)) # 2022-12-06 00:00:00
print(parser.parse(s3))  # 2022-06-12 14:35:00

## 练习:计算以下列表中连续的天数
import numpy as np
datelist = ['Oct, 2, 1869', 'Oct, 10, 1869', 'Oct, 15, 1869', 'Oct, 20, 1869','Oct, 23, 1869']
ds = [parser.parse(i) for i in datelist]
tds = np.diff(ds)
print(tds)   # [datetime.timedelta(days=8) datetime.timedelta(days=5) datetime.timedelta(days=5) datetime.timedelta(days=3)]
d = [i.days for i in tds]
print(d)  # [8, 5, 5, 3]

"""
date类
"""
# class date:
#     def __init__(self, year, month, day):
#         pass
#     def today(cls):
#         pass

# 1. date.today() 获取当前日期信息。
## 示例:如何在 Python 中获取当前日期和时间？
d = datetime.date(2022,6,12)
print(d)  # 2022-06-12
print(type(d))  # <class 'datetime.date'>

d = datetime.date.today()
print(d)  # 2022-06-12
print(type(d))  # <class 'datetime.date'>


## 练习: 如何统计两个日期之间有多少个星期六？
d1 = datetime.date(1869, 1, 2)
d2 = datetime.date(1869, 10, 2)
d_ = (d2-d1).days
print(d1.isoweekday()) # 6
print(d2.isoweekday()) # 6
print(d_//7 + 1)  # 40

"""
time类
"""
# class time:
#     def __init__(self, hour, minute, second, microsecond, tzinfo):
#         pass

## 示例: 如何使用 datetime.time() 类？
t = datetime.time(14,56,25,13600)
print(t)  # 14:56:25.013600
print(type(t))  # <class 'datetime.time'>

## 注意：
# 1. 1秒 = 1000 毫秒（milliseconds）
# 2. 1毫秒 = 1000 微妙（microseconds）

## 【练习】如何将给定日期转换为当天开始的时间？
date = datetime.date(2019, 10, 2)
dt = datetime.datetime(date.year, date.month, date.day)
print(dt)  # 2019-10-02 00:00:00

dt = datetime.datetime.combine(date, datetime.time.min)
print(dt)  # 2019-10-02 00:00:00

"""
timedelta类
timedelta 表示具体时间实例中的一段时间。你可以把它们简单想象成两个日期或时间之间的间隔。
它常常被用来从 datetime 对象中添加或移除一段特定的时间。
"""

# class timedelta(SupportsAbs[timedelta]):
#     def __init__(self, days, seconds, microseconds, milliseconds, minutes, hours, weeks,):
#         pass
#     def days(self):
#         pass
#     def total_seconds(self):
#         pass

## 【例子】如何使用 datetime.timedelta() 类？
td =datetime.timedelta(days=30)
print(td)  # 30 days, 0:00:00
print(type(td))  # <class 'datetime.timedelta'>
print(datetime.date.today())  # 2022-06-12
print(datetime.date.today() + td)  # 2022-07-12

dt1 = datetime.datetime(2022,6,12,15,12,30)
dt2 = datetime.datetime(2019, 1, 31, 10, 10, 0)
td = dt1 - dt2
print(td)  # 1228 days, 5:02:30
print(type(td))  # <class 'datetime.timedelta'>

td1 = datetime.timedelta(days=30)
td2 = datetime.timedelta(weeks=1)
td = td1 - td2
print(td)  # 23 days, 0:00:00
print(type(td))  # <class 'datetime.timedelta'>

# 如果将两个 datetime 对象相减，就会得到表示该时间间隔的 timedelta 对象。
# 同样地，将两个时间间隔相减，可以得到另一个 timedelta 对象。

