#! /usr/bin/env python
#coding=utf-8

from __future__ import print_function
from __future__ import division


def numparse(n):
    n2l = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand",
    }
    if n <= 20:
        return n2l[n]
    elif n <= 99 and n % 10 == 0:
        return n2l[n]
    elif n <= 99:
        return "%s %s" % (n2l[n//10*10], n2l[n%10])
    elif n <= 999 and n %100 == 0:
        return "%s hundred" % n2l[n//100]
    elif n <= 999:
        return "%s hundred and %s" % (n2l[n//100], numparse(n%100))
    elif n == 1000:
        return "one thousand"


total = 0
for i in range(1, 1001):
    total += len(numparse(i).replace(" ", ""))

print(total)



