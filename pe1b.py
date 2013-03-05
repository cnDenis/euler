#! /usr/bin/env python
#coding=utf-8

from __future__ import print_function
from __future__ import division

print(sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0))
