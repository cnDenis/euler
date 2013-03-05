#! /usr/bin/env python
#coding=utf-8

from __future__ import print_function
from __future__ import division

#2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

from collections import Counter


def factors(n):
    i = 2
    while n > 1:
        if n % i == 0:
            yield i
            n //= i
            i -= 1
        i += 1


cc = Counter()
for i in range(20):
    cc |= Counter(factors(i))

ss = 1
for k, v in cc.items():
    ss *= k**v
print(ss)
