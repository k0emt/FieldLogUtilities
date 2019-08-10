# Source format:
# YYYY/MM/DD,Summit,CallSign
# UTC,Freq,mode,call,summit,comment

# Target format:
# <V2> <My Callsign><My Summit> <Date> <Time> <Band> <Mode> <Their Callsign><Their Summit> <Notes or Comments>

import sys

def get_summit(entry_data):
    if len(entry_data) > 4:
        return (entry_data[4])
    return ''

def get_comment(entry_data):
    if len(entry_data) > 5:
        return(entry_data[5])
    return ''

if len(sys.argv) != 2:
    print ("usage: %s <source file name>" % sys.argv[0])
    exit(-1)

sourceFileName = sys.argv[1]
sourceFile = open(sourceFileName, "r")

# read first line to get date, summit and my callsign
firstLine = sourceFile.readline()
keydata = firstLine.rstrip().split(",")
date = keydata[0]
summit = keydata[1]
op = keydata[2]

for contact in sourceFile:
    entry_data = contact.rstrip().split(",")
    s2s = get_summit(entry_data)
    comment = get_comment(entry_data)
    print('V2,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (op, summit, date, entry_data[0],entry_data[1],entry_data[2],entry_data[3],s2s,comment))

sourceFile.close()