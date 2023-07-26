import sys
import re
from datetime import datetime


def readAndParseDate(date):
    r = []
    for d in date:
        r.append(int(d))
    return r

# TODO: wrong input message vvv
n = len(sys.argv)
print("Total arguments passed:", n)

# open files
input = open(sys.argv[1], "r")
output = open("output.txt", "w")

# process dates
d1 = readAndParseDate(sys.argv[2].split("."))
d2 = readAndParseDate(sys.argv[3].split("."))
date1 = datetime(2000+d1[0], d1[1], d1[2], d1[3], d1[4], d1[5])
date2 = datetime(2000+d2[0], d2[1], d2[2], d2[3], d2[4], d2[5])


for l in input:  
    match = re.search(r"\[(\d{2}/\d{2}/\d{2}), (\d{2}:\d{2}:\d{2})\]", l)
    if match:
        date_str, time_str = match.group(1), match.group(2)
        date_obj = datetime.strptime(date_str + " " + time_str, "%d/%m/%y %H:%M:%S")
        if date1 < date_obj and date_obj < date2:
            output.write(l)

input.close()
output.close()

