# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for i in range(n - 1):
        previous, current = current, previous + current

    return current % m

def Huge_Fib(n,m):
    # Taken from stackoverflow, used for testing results as I do not understand the math behined this code
    # Initialize a matrix [[1,1],[1,0]]    
    v1, v2, v3 = 1, 1, 0  
    # Perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(n)[3:]:
        calc = (v2*v2) % m
        v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
        if rec == '1': v1, v2, v3 = (v1+v2) % m, v1, v2
    return v2

def myCode(n, m):
    if n <= 1:
        return n
    previous = 0
    current = 1
    pisiano = [0, 1]

    for i in range(n - 1):
        previous, current = current, previous + current
        pisiano.append(current % m)
        if pisiano[len(pisiano) - 1] == 1 and pisiano[len(pisiano) - 2] == 0:
            return pisiano[n % (len(pisiano) - 2)]
    return pisiano[len(pisiano) -1]
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(myCode(n, m))
