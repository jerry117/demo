#! /usr/bin/python
# -*- coding:utf-8 -*-

# 一个简单的reportlab程序
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100)
s = String(50, 50, 'hello, world!', textAnchor='middle')

d.add(s)

renderPDF.drawToFile(d, 'hello.pdf', 'a simple pdf file')
