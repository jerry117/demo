#! /usr/bin/python
# -*- coding:utf-8 -*-

import pymysql
import time

try:
    conn = pymysql.connect(host='localhost', user='root', passwd='asdf', db='test', port=3306)
    cur = conn.cursor()
    cur.execute('select * from orders')
    kk =list(cur)
    for j in range(0, len(kk)):
        print kk[j]
    cur.close()
    conn.close()
except pymysql.Error, e:
    print 'mysql error %d: %s' %(e.args[0], e.args[1])