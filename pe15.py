#! /usr/bin/env python
#coding=utf-8

from __future__ import print_function
from __future__ import division

grid = 20

step = {0: 1}
for i in range(1, grid+2):
    newstep = {}
    for j in range(i):
        if j == 0 or j == i-1:
            newstep[j] = 1
        else:
            newstep[j] = step[j] + step[j-1]
    step = newstep

for i in range(grid, 0, -1):
    newstep = {}
    for j in range(i):
        newstep[j] = step[j] + step[j+1]
    step = newstep

print(step[0])
