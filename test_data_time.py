#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2017/7/27 下午7:53
# @Author   : jerry
# @File     : test_data_time.py
# @Software : PyCharm

from datetime import date
from datetime import time
from datetime import datetime


if __name__ == "__main__":
    today = date.today()
    print ("今天是 %s" % today)

    print ("今天是 %s %s %s" %(today.day, today.month, today.year))

    weekday_num = today.weekday()
    print ("今天weekday是 %s" % weekday_num)

    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    print ("今天是 %s" % weekdays[weekday_num])
    print ("-" * 30)

    today_now = datetime.now()
    print ("现在是 %s" % today_now)

    t = time(hour=12, minute=20, second=30, microsecond=200)
    print ("我们自己造的时间是 %s" % t)

    d = datetime(year=2008, month=8, day=8, hour=8, minute=8, second=8)
    print ("我们自己造的日期时间 %s" % d)