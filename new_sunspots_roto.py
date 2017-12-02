#! /usr/bin/python
# -*- coding:utf-8 -*-
'''
# data source

:Predicted_Sunspot_Numbers_and_Radio_Flux: Predict.txt
:Created: 2017 Nov 06 0400 UTC
# Prepared by the U.S. Dept. of Commerce, NOAA, Space Weather Prediction Center (SWPC).
# Please send comments and suggestions to swpc.webmaster@noaa.gov
#
# Sunspot Number: S.I.D.C. Brussels International Sunspot Number.
# 10.7cm Radio Flux value: Penticton, B.C. Canada.
# Predicted values are based on the consensus of the Solar Cycle 24 Prediction Panel.
#
# See the README3 file for further information.
#
# Missing or not applicable data:  -1
#
#         Predicted Sunspot Number And Radio Flux Values
#                     With Expected Ranges
#
#         -----Sunspot Number------  ----10.7 cm Radio Flux----
# YR MO   PREDICTED    HIGH    LOW   PREDICTED    HIGH    LOW
#--------------------------------------------------------------
2017 05        14.7    15.7    13.7       77.9    78.9    76.9
2017 06        15.4    17.4    13.4       77.9    78.9    76.9
2017 07        15.8    18.8    12.8       77.9    79.9    75.9
2017 08        16.0    21.0    11.0       77.7    80.7    74.7
2017 09        16.3    21.3    11.3       77.6    81.6    73.6
2017 10        16.4    22.4    10.4       77.2    81.2    73.2
2017 11        16.3    23.3     9.3       76.8    81.8    71.8
2017 12        16.6    23.6     9.6       76.6    82.6    70.6
2018 01        16.7    24.7     8.7       76.2    83.2    69.2
2018 02        16.5    25.5     7.5       75.5    83.5    67.5
2018 03        15.6    24.6     6.6       74.3    82.3    66.3
2018 04        15.1    25.1     5.1       73.0    82.0    64.0
2018 05        14.8    24.8     4.8       72.3    81.3    63.3
2018 06        13.7    23.7     3.7       71.3    80.3    62.3
2018 07        12.9    22.9     2.9       70.6    79.6    61.6
2018 08        12.2    22.2     2.2       69.9    78.9    60.9
2018 09        11.5    21.5     1.5       69.2    78.2    60.2
2018 10        10.8    20.8     0.8       68.6    77.6    60.0
2018 11        10.1    20.1     0.1       68.0    77.0    60.0
2018 12         9.5    19.5     0.0       67.4    76.4    60.0
2019 01         8.9    18.9     0.0       66.9    75.9    60.0
2019 02         8.3    18.3     0.0       66.3    75.3    60.0
2019 03         7.8    17.8     0.0       65.9    74.9    60.0
2019 04         7.3    17.3     0.0       65.4    74.4    60.0
2019 05         6.8    16.8     0.0       65.0    74.0    60.0
2019 06         6.4    16.4     0.0       64.5    73.5    60.0
2019 07         5.9    15.9     0.0       64.1    73.1    60.0
2019 08         5.5    15.5     0.0       63.8    72.8    60.0
2019 09         5.1    15.1     0.0       63.4    72.4    60.0
2019 10         4.8    14.8     0.0       63.1    72.1    60.0
2019 11         4.4    14.4     0.0       62.8    71.8    60.0
2019 12         4.1    14.1     0.0       62.5    71.5    60.0
'''

from urllib import urlopen
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF

URL = 'http://services.swpc.noaa.gov/text/predicted-sunspot-radio-flux.txt'
COMMENT_CHARS = '#:'

drawing = Drawing(400, 200)
data = []
for line in urlopen(URL).readlines():
    if not line.isspace() and not line[0] in COMMENT_CHARS:
        data.append([float(n) for n in line.split()])

pred = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[0]+row[1]/12.0 for row in data]

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [zip(times, pred), zip(times, high), zip(times, low)]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)
drawing.add(String(250, 150, 'Sunspots', fontSize=14, fillColor=colors.red))


renderPDF.drawToFile(drawing, 'report2.pdf', 'Sunspots')
