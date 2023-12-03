# 1. 距离你出生那天过去多少天了？
from datetime import datetime,timedelta,timezone,date
import re
from dateutil import parser
dt1 = date(2022,6,12)
dt2 = date(1999,7,10)
print(dt1-dt2)  # 8373 days, 0:00:00

# 2. 距离你今年的下一个生日还有多少天？
dt1 = date(2022,7,10)
dt2 = date(2022,6,12)
print(dt1-dt2)  # 28 days, 0:00:00


# 3. 将距离你今年的下一个生日的天数转换为秒数。
print((dt1-dt2).total_seconds())  # 2419200.0


# 4.假设你获取了用户输入的日期和时间如2020-1-21 9:01:30 ，以及一个时区信息如UTC+5:00 ，均是str ，请编写一个函数将其转换为timestamp：
"""
Input file
example1: dt_str='2020-6-1 08:10:30', tz_str='UTC+7:00'
example2: dt_str='2020-5-31 16:10:30', tz_str='UTC-09:00'
Output file
result1: 1590973830.0
result2: 1590973830.0
"""

def Date2Stamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    time_zone_num = re.match('UTC([+|-][\d]{1,2}):00', tz_str).group(1)
    time_zone = timezone(timedelta(hours=int(time_zone_num)))
    return datetime.timestamp(dt.replace(tzinfo=time_zone))

t1 = Date2Stamp(dt_str='2020-6-1 08:10:30', tz_str='UTC+7:00')
print(t1)  # 1590973830.0
t2 = Date2Stamp(dt_str='2020-5-31 16:10:30', tz_str='UTC-09:00')
print(t2) # 1590973830.0


# 5.编写Python程序以选择指定年份的所有星期日。
"""
Input file
2020
Output file
2020-01-05
2020-01-12
2020-01-19
2020-01-26
2020-02-02
-----
2020-12-06
2020-12-13
2020-12-20
2020-12-27
"""
def FindSunday(year):
    d_start = date(year=year,month=1,day=1)
    d_start += timedelta(days=(6-d_start.weekday())) # weekday 输出 0-6
    while(d_start.year==year):
        yield d_start
        d_start += timedelta(days=7)


for i in FindSunday(2020):
    print(i)

