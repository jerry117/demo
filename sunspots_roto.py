#! /usr/bin/python
# -*- coding:utf-8 -*-

from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

data = [
    (2007, 8, 113.2, 114.2, 112.2),
    (2007, 9, 112.8, 115.8, 109.8),
    (2007, 10, 111.0, 116.0, 106.0),
    (2007, 11, 113.2, 114.2, 112.2),
    (2007, 12, 113.2, 114.2, 112.2),
    (2008, 1, 113.2, 114.2, 112.2),
    (2008, 2, 113.2, 114.2, 112.2),
    (2008, 3, 113.2, 114.2, 112.2),
    (2008, 4, 113.2, 114.2, 112.2),
    (2008, 5, 113.2, 114.2, 112.2),
]

drawing = Drawing(200, 150)

pred = [row[2]-40 for row in data]
high = [row[3]-40 for row in data]
low = [row[4]-40 for row in data]
times = [200*((row[0]+row[1]/12.0) - 2007)-110 for row in data]

drawing.add(PolyLine(zip(times, pred), strokeColor=colors.blue))
drawing.add(PolyLine(zip(times, high), strokeColor=colors.red))
drawing.add(PolyLine(zip(times, low), strokeColor=colors.green))
drawing.add(String(65, 115, 'Sunspots', fontSize=18, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')