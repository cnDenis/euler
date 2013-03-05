#! /usr/bin/env python
#coding=utf-8

#A permutation is an ordered arrangement of objects. For example, 3124 is
#     one possible permutation of the digits 1, 2, 3 and 4. If all of the
#         permutations are listed numerically or alphabetically, we call it
#             lexicographic order. The lexicographic permutations of 0, 1
#                 and 2 are:
#
#012   021   102   120   201   210
#
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
# 4, 5, 6, 7, 8 and 9?


from __future__ import print_function
from __future__ import division

num = 1000000

def fac(n):
    if n == 0:
        return 1
    t = 1
    for i in range(1, n+1):
        t *= i
    return t

nums = [i for i in range(10)]
out = []
num -= 1 #因为从0开始计数
for i in range(10):
    t = fac(9-i)
    n = num // t
    num %= t
    out.append(nums.pop(n))

print("".join(map(str,out)))


