# use regex to find emails as alternative to email2.py
import re
fhand = open('mbox-short.txt', 'r', encoding='UTF-8')

for line in fhand:
    line =line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
    