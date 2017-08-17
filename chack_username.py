#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2017/8/6 下午10:22
# @Author   : jerry
# @File     : chack_username.py
# @Software : PyCharm

database = [['albert', '1234'], ['dilbert', '4242'], ['smith', '7524'], ['jones', '9843']]
username = raw_input('user name: ')
pin = raw_input('pin code: ')

if [username, pin] in database:
    print 'access granted'
