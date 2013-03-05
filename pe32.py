#! /usr/bin/env python
#coding=utf-8

from __future__ import print_function
from __future__ import division

def n3(n):
    """十进转3进制"""
    t = []
    while n > 0:
        t.append(n%3)
        n = n // 3
    t.reverse()
    return t

def (${2:}):
    ${0}

for i in range(3**9):
