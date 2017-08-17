#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2017/7/29 下午5:40
# @Author   : jerry
# @File     : test_strftime.py
# @Software : PyCharm

import time


if __name__ == "__main__":
    # time.strftime(format[, t])
    localtime = time.asctime(time.localtime())
    print ("当前默认日期时间格式: %s" %localtime)


    print ("24小时制全格式: %s" % time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime()))

    print ("12小时制缩写格式: %s" % time.strftime("%Y-%m-%d %I:%M:%S %a", time.localtime()))


    print ("带a.m或p.m 24小时制全格式: %s" % time.strftime("%Y-%m-%d %H:%M:%S %p %A", time.localtime()))


    print ("带时区的全格式: %s" % time.strftime("%Y-%m-%d %H:%M:%S %p %A %z", time.localtime()))

    # 格式乱排下试试
    print("随意排格式：%s" % time.strftime("%A %Y-%d-%m %p %H:%M:%S %z", time.localtime()))