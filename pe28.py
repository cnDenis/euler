#! /usr/bin/env python
#coding=utf-8

#Starting with the number 1 and moving to the right in a clockwise direction
#     a 5 by 5 spiral is formed as follows:
#
#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13
#
#It can be verified that the sum of the numbers on the diagonals is 101.
#
#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?
#

from __future__ import print_function
from __future__ import division

spi = 1001

n = 1
t = 1
for i in range(1, spi//2 + 1):
    for j in range(4):
        n += 2*i
        t += n

print(t)
