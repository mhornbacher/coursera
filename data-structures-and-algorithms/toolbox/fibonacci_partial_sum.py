# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current  = 1

    for i in range(from_ - 1):
        previous, current = current, previous + current

    sum = current

    for i in range(to - from_):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum_fast(n):
    result = [1, 2, 4, 7, 2, 0, 3, 4, 8, 3, 2, 6, 9, 6, 6, 3, 0, 4, 5, 0, 6, 7, 4, 2, 7, 0, 8, 9, 8, 8, 7, 6, 4, 1, 6, 8, 5, 4, 0, 5, 6, 2, 9, 2, 2, 5, 8, 4, 3, 8, 2, 1, 4, 6, 1, 8, 0, 9, 0, 0]
    return(result[n % 60 - 1])

def fibonacci_partial_sum_fast(m, n):
    if n <= 1:
        return n

    n1 = fibonacci_sum_fast(n)
    m1 = fibonacci_sum_fast(m)
    total = n1 - m1
    print(n1)
    print(m1)
    print(total)
        
    return total % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum_fast(from_, to))
