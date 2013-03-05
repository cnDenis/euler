#! /usr/bin/env python
#coding=utf-8

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.
#

from __future__ import print_function
from __future__ import division

lim = 2000000
m = list(xrange(2, lim))

total = 0
n = m[0]
while m:
    total += n
    for i in xrange(0, lim, n):
        try:
            m.remove(i)
            n = m[0]
        except:
            pass

print(total)
