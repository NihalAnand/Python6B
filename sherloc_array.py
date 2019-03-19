#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def arraySherlock(a):   
    
    left_in = 0
    right_in = len(a) - 1
     
    left_sum = a[left_in]
    right_sum = a[right_in]
     
    while left_in != right_in:
        if left_sum < right_sum:
            left_in += 1
            left_sum += a[left_in]
        else:
            right_in -= 1
            right_sum += a[right_in]
     
    return left_sum == right_sum
     
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if arraySherlock(a):
            print ("YES")
        else:
            print ("NO")
