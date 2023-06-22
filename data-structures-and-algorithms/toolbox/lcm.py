# Uses python3
import sys

def gcd_elucid(a,b):
    if b == 0:
        return a
    else:
        return gcd_elucid(b, a % b)

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm(a, b):
    return (a * b) // gcd_elucid(a, b)
    

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(int(lcm(a, b)))

