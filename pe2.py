#! /usr/bin/env python
#coding=utf-8

#Each new term in the Fibonacci sequence is generated by adding the previous
#     two terms. By starting with 1 and 2, the first 10 terms will be:
#
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
#By considering the terms in the Fibonacci sequence whose values do not exceed
#four million, find the sum of the even-valued terms.
#

from __future__ import print_function
from __future__ import division

a = 2
b = 1
total = 2

while a < 4e6:
    t = a
    a += b
    if a % 2 == 0:
        total += a
    b = t

print(total)
