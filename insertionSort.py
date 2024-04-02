import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    right = arr[n - 1]
    for i in range(n - 2, -1, -1):
        if arr[i] > right:
            arr[i + 1] = arr[i]
            print(*arr)
        else:
            arr[i + 1] = right
            print(*arr)
            return
    arr[0] = right
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
