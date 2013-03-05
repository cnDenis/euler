#! /usr/bin/env python
#coding=utf-8

#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?
#

from __future__ import print_function
from __future__ import division


def findpf(n):
    "这个算法是错的, n**0.5可能会跳过其最大的约数，若改成n/2则运算量过大"
    for i in range(int(n ** 0.5) + 1, 0, -1):
        if i == 1:
            print(n)
        elif n % i == 0:
            findpf(i)
            break


def findpf2(n):
    nsq = int(n ** 0.5)
    for i in range(2, nsq + 1): #每次从2开始是浪费时间的做法
        if i == nsq:
            print(n)
        elif n % i == 0:
            findpf2(n // i)
            break


def isprime(n):
    nsq = int(n ** 0.5)
    for i in range(2, nsq + 1):
        if n % i == 0:
            return False
        elif i == nsq:
            return True


findpf2(600851475143)
print(isprime(5))

#C代码：
#__int64 number = 317584931803;
#	int divisor = 2;
#	while (number > 1) {
#		if (0 == (number % divisor)) {
#			number /= divisor;
#			divisor--;
#		}
#		divisor++;
#	}
#	// [i]divisor[/i] is the answer
