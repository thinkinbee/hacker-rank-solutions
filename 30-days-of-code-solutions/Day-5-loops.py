#!/bin/python

import sys


n = int(raw_input().strip())

for i in range(1,11):
    print '{0} x {1} = {2}'.format(n,i,n*i)
