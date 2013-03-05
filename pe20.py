#! /usr/bin/env python
#coding=utf-8

#n! means n  (n  1)  ...  3  2  1
#
#For example, 10! = 10  9  ...  3  2  1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
#Find the sum of the digits in the number 100!
#

from __future__ import print_function
from __future__ import division

def jiechen(n):
    t = 1
    for i in range(1, n+1):
        t *= i
    return t

print(sum(map(int, str(jiechen(100)))))