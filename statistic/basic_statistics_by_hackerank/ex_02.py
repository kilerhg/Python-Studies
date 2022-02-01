#!/bin/python3

import math
import os
import random
import re   
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    total_w = sum(W)
    list_values = []
    for item in zip(X, W):
        list_values.append(item[0] * item[1])
    total_x = sum(list_values) / total_w
    print(round(total_x, 1))
    
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
