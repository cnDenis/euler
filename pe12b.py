#! /usr/bin/env python
#coding=utf-8

from __future__ import print_function
from __future__ import division
from collections import Counter

def trinum():
    i = 1
    t = 0
    while True:
        t += i
        yield t
        i += 1

def divcnt(n):
    i = 2
    div = []
    while n > 1:
        while n % i == 0:
            div.append(i)
            n //= i
        i += 1
    cc = Counter(div)
    t = 1
    for k, v in cc.items():
        t *= v+1
    return t


t = trinum()
c = 0
while c < 500:
    tt = t.next()
    c = divcnt(tt)
print(tt)


#76576500
#         258612 function calls (258609 primitive calls) in 8.696 seconds
#
#   Ordered by: internal time
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    12375    7.796    0.001    8.535    0.001 pe12b.py:16(divcnt)
#    12375    0.207    0.000    0.529    0.000 collections.py:469(update)
