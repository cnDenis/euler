#! /usr/bin/env python
#coding=utf-8

#The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#
#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
#


from __future__ import print_function
from __future__ import division

def pow(n):
    t = 1
    for i in range(n):
        t *= n
        t %= 100000000000
    return t

t = 0
for i in range(1, 1001):
    t += pow(i)

print(str(t)[-10:])
