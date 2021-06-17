import codecs
import os
import time
import importlib
import sys

from Bot_testing import GetData

getdata = GetData()

def grabTwoPart(str):
    elementName = ''
    key = ''
    data = ''
    equalyet = 0
    for i in range(0, len(str)):
        if str[i] == '=':
            equalyet += 1
            continue
        if equalyet == 0:
            elementName += str[i]
        elif equalyet == 1:
            key += str[i]
        else:
            data += str[i]

    elementName = elementName.rstrip("\n")
    key = key.rstrip("\n")
    data = data.rstrip("\n")

    return (elementName, key, data)

if __name__ == "__main__":

    fi = open("INPUT.txt", "r", encoding="utf8")
    info = {}

    while True:
        line = fi.readline()
        if not line:
            break
        data = grabTwoPart(line)

        info[data[1]] = (data[0], data[2])

    getdata.build(info)
    getdata.process()

    print("Done.")
