import os
import re
import subprocess
import time

response = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

ping = ping[0].replace(',', '.')
download = download[0].replace(',', '.')
upload = upload[0].replace(',', '.')

try:
    f = open('/home/pi/Desktop/SpeedTestAnalyzer/speedtest/speedtest.csv', 'a+')
    if os.stat('/home/pi/Desktop/SpeedTestAnalyzer/speedtest/speedtest.csv').st_size == 0:
            f.write('DateTime,Ping (ms),Download (Mbit/s),Upload (Mbit/s)\r\n')
except:
    pass

f.write('{},{},{},{}\r\n'.format(time.strftime('%Y-%m-%d %H:%M'), ping, download, upload))
