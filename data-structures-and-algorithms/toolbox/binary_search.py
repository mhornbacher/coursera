# Uses python3
import sys
from math import floor

def binary_search(array, target):
    # Set lower and upper
    lower = 0
    upper = len(array)
    #While there is still space in the array
    while lower < upper:
        # Set the midpoint to the middle of what remains
        mid = lower + (upper - lower) // 2
        val = array[mid]    # Get the value at that point

        if target == val: # If we found the object
            return mid # return the index
        elif target > val:  # if it is greater
            if lower == mid: # Catch this bug
                break
            lower = mid # throw away the first half of the array
        elif target < val: # if it is before this section of the array
            upper = mid # throw awway the upper half of the array
    return -1 # return -1 if there is no index

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')

