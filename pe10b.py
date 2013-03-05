#! /usr/bin/env python
#coding=utf-8

from __future__ import print_function
from __future__ import division

def isprime(n):
    for i in range(2, int(n ** 0.5)+1):
        if n%i == 0:
            return False
    return True


total = 2
for i in xrange(3, 2000000, 2):
    if isprime(i):
        total += i

print(total)

#2000010 function calls in 55.669 seconds