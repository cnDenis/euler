#! /usr/bin/env python
#coding=utf-8

#If a box contains twenty-one coloured discs, composed of fifteen blue discs
# and six red discs, and two discs were taken at random, it can be seen that
# the probability of taking two blue discs, P(BB) = (15/21)(14/20) = 1/2.
#
#The next such arrangement, for which there is exactly 50% chance of taking
# two blue discs at random, is a box containing eighty-five blue discs and
# thirty-five red discs.
#
#By finding the first arrangement to contain over 1012 = 1,000,000,000,000
# discs in total, determine the number of blue discs that the box would contain.


from __future__ import print_function
from __future__ import division
from fractions import Fraction
import sys

dics = 1000

while True:
    m = dics
    n = 0
    while m > n:
        k = (m+n) // 2
        p = Fraction(k*(k-1), dics*(dics-1))
        if p > 0.5:
            m = k
        elif p < 0.5:
            n = k + 1
        else:
            print(k)
            sys.exit()
    dics += 1


