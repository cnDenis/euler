#! /usr/bin/env python
#coding=utf-8

from __future__ import print_function
from __future__ import division

with open("data67-triangle.txt") as fp:
    mat = []
    for line in fp:
        li = []
        for n in line.split():
            li.append(int(n))
        mat.append(li)

msum = mat[-1]

for row in reversed(mat[:-1]):
    newsum = []
    for i in range(len(row)):
        newsum.append(row[i] + max([msum[i], msum[i+1]]))
    msum = newsum

print(msum)
