# Uses python3
import sys
import random

def optimal_summands(n):
    if n == 2:
        return [2]
    summands = [1]
    while n - (sum(summands) + (summands[-1] + 1)) > summands[-1] + 1:
        summands.append(summands[-1] + 1)
    if n - sum(summands) > 0:
        summands.append(n - sum(summands))
            
    return summands


def optimal_summands_fast(n):
    summands = []
    k = n
    l = 1
    while k > 2*l:
        summands.append(l)
        k = k - l
        l = l + 1
    summands.append(k)
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands_fast(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')


