#!/bin/python

import sys

def build_bin(n):
    b_repr = []
    while n > 0:
        rem = n % 2
        b_repr.append(rem)
        n = n / 2 
    b_repr.reverse()
    return b_repr

def calc_digits(bin_l):
    curr_high = 0
    runng_high = 0
    for x in bin_l:
        if x:
            runng_high = runng_high + 1
        else:
            if curr_high <= runng_high:
                curr_high = runng_high
                runng_high = 0
            else:
                runng_high = 0
            continue
    if curr_high > runng_high:
        return curr_high
    else:
        return runng_high
    
if __name__ == '__main__':
    n = int(raw_input().strip())
    #build the binary representaion
    binary_repr = build_bin(n)
    print calc_digits(binary_repr)