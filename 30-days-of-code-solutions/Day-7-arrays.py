#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

str_out = ""
for i in range(n):
    str_out = str_out + str(arr[n-i-1])+" "
print str_out
