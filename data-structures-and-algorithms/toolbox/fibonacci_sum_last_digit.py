# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    total      = 1

    for i in range(n - 1):
        previous, current = current, previous + current
        total += current

    return total % 10


def fibonacci_sum_fast(n):

    result = [1, 2, 4, 7, 2, 0, 3, 4, 8, 3, 2, 6, 9, 6, 6, 3, 0, 4, 5, 0, 6, 7, 4, 2, 7, 0, 8, 9, 8, 8, 7, 6, 4, 1, 6, 8, 5, 4, 0, 5, 6, 2, 9, 2, 2, 5, 8, 4, 3, 8, 2, 1, 4, 6, 1, 8, 0, 9, 0, 0]
    return(result[n % 60 - 1])

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_fast(n))
