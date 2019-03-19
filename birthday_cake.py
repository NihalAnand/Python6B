#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    re=max(ar)
    count=0
    for i in range (len(ar)):
        if(re==ar[i]):
            count+=1
    
    print(count)
        

if __name__ == '__main__':
    

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    #print(result)
    