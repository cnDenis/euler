#! /usr/bin/env python
#coding=utf-8

#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name
# score.
#
#For example, when the list is sorted into alphabetical order, COLIN, which
# is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938  53 = 49714.
#
#What is the total of all the name scores in the file?

from __future__ import print_function
from __future__ import division

orda = ord("A")-1
total = 0
names = []
with open("data22-names.txt") as fp:
    pos = 1
    for line in fp.read().split(","):
        names.append(line.strip('"'))
    names.sort()
    for line in names:
        point = sum([(ord(s)-orda) for s in line])
        score = point * pos
        pos += 1
        total += score
        print(line, point)


print(total)
