#! /usr/bin/env python
#coding=utf-8

#The following iterative sequence is defined for the set of positive integers:
#
#n  n/2 (n is even)
#n  3n + 1 (n is odd)
#
#Using the rule above and starting with 13, we generate the following sequence:
#
#13  40  20  10  5  16  8  4  2  1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is
# thought that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?
#
#NOTE: Once the chain starts the terms are allowed to go above one millio

from __future__ import print_function
from __future__ import division

MAX = 1000000


def chain(n):
    while n > 1:
        if n % 2 == 0:
            t = n // 2
            yield t
            n = t
        else:
            t = n * 3 + 1
            yield t
            n = t

def main():
    maxi = 0
    maxc = 0
    nums = {i:i for i in range(MAX)}
    for i in xrange(MAX-1, MAX//2, -2):
        count = 0
        if nums[i]:
            for n in chain(i):
                if n < MAX:
                    nums[i] = 0
                count += 1
            if count > maxc:
                maxc = count
                maxi = i

    print(maxi)

def testchain():
    for i in chain(13):
        print(i)

main()


#837799
#         132434439 function calls in 411.100 seconds
#
#   Ordered by: internal time
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#132434424  208.684    0.000  208.684    0.000 pe14b.py:26(chain)
#        1  202.324  202.324  411.089  411.089 pe14b.py:37(main)
