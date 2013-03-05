#! /usr/bin/env python
#coding=utf-8

#A palindromic number reads the same both ways. The largest palindrome made
#from the product of two 2-digit numbers is 9009 = 91  99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

from __future__ import print_function
from __future__ import division

import sys

def pal(n):
    nn = n
    while n > 0:
        nn = nn * 10 + n % 10
        n //= 10
    return nn

for i in range(999, 100, -1):
    n = pal(i)
    for j in range(999, 500, -1):
        if n % j == 0 and 100 <= n // j <= 999:
            print(n)
            sys.exit()
