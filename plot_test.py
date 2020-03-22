# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
#import clockplotter as cp

# THIS IS TEST DATA THAT I KNOW WORKS, FOR TRYING NEW CODE ADDITIONS
#times = pd.date_range(start='2018-04-28', end='2018-04-29', freq='10min')
#x = np.array(times)
#x = np.linspace(0, 2*np.pi, 400)
#y1 = np.sin(x**2)
#y2 = np.sin(x**3)

# Reading a csv file from my desktop. Figure out how to find this csv
# file on whatever Raspberry Pi this code downloads onto.

#df = pd.read_csv("C:\Users\BenK\Desktop\\testData.csv")
df = pd.read_csv("/home/pi/Desktop/SpeedTestAnalyzer/speedtest/speedtest.csv")

# Instantiate plots
ax = plt.subplot(111)

# Reads different columns from csv file. Can't figure out yet how to
# format the X-axis for date or time yet. To do soon!
x1 = df['DateTime']
y1 = df[' Ping (ms)']
y2 = df[' Download (Mbit/s)']
y3 = df[' Upload (Mbit/s)']

for i in range(len(x1)):
    x1[i] = datetime.datetime.strptime(x2[i], "%Y-%m-%d %H:%M")


ax.plot(x1, y1, 'r', linewidth=2)
ax.plot(x1, y2, 'g', linewidth=3)
ax.plot(x1, y3, 'b', linewidth=4)
ax.set_title('Daily Internet Speed')

# Adds legend for the different colored lines
red_line = mlines.Line2D([], [], color='red', linewidth=2, label='Ping (ms)')
green_line = mlines.Line2D([], [], color='green', linewidth=3, label='Download (Mbits/s)')
blue_line = mlines.Line2D([], [], color='blue', linewidth=4, label='Upload (Mbits/s)')

plt.legend(handles=[red_line, green_line, blue_line],
           bbox_to_anchor=(1,1), loc='upper left',
            bbox_transform=plt.gcf().transFigure)

plt.gcf().autofmt_xdate()
plt.show()
