# Uses python3
import sys

def get_change(m):
    result = 0
    while m >= 10:
        m -= 10
        result += 1
    if m >= 5:
        m-= 5
        result += 1
    result = result + m
    return result

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
