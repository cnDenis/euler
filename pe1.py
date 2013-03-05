#! /usr/bin/env python
#coding=utf-8

#Problem 1
#05 October 2001
#
#If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.
#

from __future__ import print_function
from __future__ import division

MAX = 1000

total = 0

for i in range(MAX):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(total)
