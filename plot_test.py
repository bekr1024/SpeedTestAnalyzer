# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import sys

# Filepath for reading CSV data. Windows filepath is for testing on my laptop.
#df = pd.read_csv("C:\Users\BenK\Desktop\\testData.csv")
df = pd.read_csv("/home/pi/Desktop/SpeedTestAnalyzer/speedtest/speedtest.csv")

# Instantiate plots
ax = plt.subplot(111)

# Read in specified date for plot evaluation.
spec_date = sys.argv[1]
#spec_date = "2018-04-22" # This is test data for Desktop testData.csv

# Creates new arrays to place only date-specific data.
x1 = []
y1 = []
y2 = []
y3 = [] 

for i in range(len(df['DateTime'])):
    j = 0
    if(df['DateTime'][i][0:10:] == spec_date):
        x1.append(df['DateTime'][i])
        y1.append(df['Ping (ms)'][i])
        y2.append(df['Download (Mbit/s)'][i]) 
        y3.append(df['Upload (Mbit/s)'][i])
        j += 1

for i in range(len(x1)):
    x1[i] = datetime.datetime.strptime(x1[i], "%Y-%m-%d %H:%M")


ax.plot(x1, y1, 'r', linewidth=2)
ax.plot(x1, y2, 'g', linewidth=3)
ax.plot(x1, y3, 'b', linewidth=4)
ax.set_title('Daily Internet Speed ' + spec_date)

# Adds legend for the different colored lines
red_line = mlines.Line2D([], [], color='red', linewidth=2, label='Ping (ms)')
green_line = mlines.Line2D([], [], color='green', linewidth=3, label='Download (Mbits/s)')
blue_line = mlines.Line2D([], [], color='blue', linewidth=4, label='Upload (Mbits/s)')

plt.legend(handles=[red_line, green_line, blue_line],
           bbox_to_anchor=(1,1), loc='upper left',
            bbox_transform=plt.gcf().transFigure)

plt.gcf().autofmt_xdate()

# Filenamefor image to save to. Windows filepath is for testing on my laptop.
#filename = "C:\\Users\\BenK\\Desktop\\" + str(spec_date) + ".png"
filename = "/home/pi/Desktop/SpeedTestAnalyzer/speedtest/" + str(spec_date) + ".png"

plt.savefig(filename, dpi=400, facecolor='w', edgecolor='w',
                  orientation='portrait', papertype='a0', format='png',
                  transparent=False, bbox_inches=None, pad_inches=0.1,
                  frameon=None)
