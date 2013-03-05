#! /usr/bin/env python
#coding=utf-8

#照抄Jalfor的程序

from __future__ import print_function
from __future__ import division

primes = [2, 3]
num = 5
while num < 2000000:
    for p in primes:
        if num % p == 0:
            break
        elif p*p > num:
            primes.append(num)
            break #这个break是必要的，否则会把刚加入的元素再放入p里
    num += 2

print(sum(primes))

#148944 function calls in 16.270 seconds