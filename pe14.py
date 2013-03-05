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
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
# that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?
#
#NOTE: Once the chain starts the terms are allowed to go above one millio

from __future__ import print_function
from __future__ import division

MAX = 100


def prenum(n):
    yield 2*n
    if (n-1) % 3 == 0 and (n-1) % 6 != 0 and n>4:
        yield (n-1)//3

treelt = 1
tree = [1, ]
pos = 0
while treelt < MAX - 1:
    for n in prenum(tree[pos]):
        if n not in tree:
            tree.append(n)
            if n < MAX:
                treelt += 1
    pos += 1

print(tree[-2:])
print(tree)
print(len(tree))
