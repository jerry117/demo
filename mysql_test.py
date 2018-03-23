#! /usr/bin/python
# -*- coding:utf-8 -*-

import pymysql
import time

# 数据库中文乱码需要设置charset字段在connect过程中。

try:
    db = pymysql.connect(host='localhost', user='root', passwd='asdf', db='test', port=3306)
# 获取游标
    cur = db.cursor()
    sql = 'select * from orders'
    cur.execute(sql)
# 合并一下SQL
    db.commit() 
    kk =list(cur)
    for j in range(0, len(kk)):
        print kk[j]
    cur.close()
    db.close()
# 捕获一下数据库的错误
except pymysql.Error, e:
    print 'mysql error %d: %s' %(e.args[0], e.args[1])
