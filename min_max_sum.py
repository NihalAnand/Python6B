

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    maxx=max(arr)
    minn=min(arr)
    mini=arr.copy()
    mini.remove(maxx)
    maxi=arr.copy()
    maxi.remove(minn)

    sum_min=sum(mini)
    sum_max=sum(maxi)

    print(sum_min,sum_max)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
