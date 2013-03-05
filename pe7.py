#! /usr/bin/env python
#coding=utf-8

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
#What is the 10 001st prime number?

from __future__ import print_function
from __future__ import division


def isprime(n):
    for i in range(2, int(n ** 0.5)+1):
        if n%i == 0:
            return False
    return True

count = 0
n = 2
while count < 10001:
    if isprime(n):
        count += 1
    n += 1
print(n-1)
