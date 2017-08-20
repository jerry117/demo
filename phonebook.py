#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2017/8/17 下午11:07
# @Author   : jerry
# @File     : phonebook.py
# @Software : PyCharm

people = {
    'alice':{
        'phone': '123456',
        'addr': 'foo drive 23'
    },
    'beth':{
        'phone': '9527',
        'addr': 'bar street 12'
    },
    'cecil':{
        'phone': '10086',
        'addr': 'baz avenue 90'
    }
}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = raw_input('name: ')
request = raw_input('phone number (p) or address (a)? ')

key = request
if request == 'p':
    key = 'phone'

if request == 'a':
    key = 'addr'

person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print "%s's %s is %s." % (name, label, result)

# if name in people :
#     print "%s's %s is %s." % (name, labels[key], people[name][key])
