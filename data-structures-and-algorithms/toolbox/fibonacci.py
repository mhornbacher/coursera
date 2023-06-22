# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        fib_array = [0, 1]
        for i in range(2, n + 1):
            fib_array.append(fib_array[i-1] + fib_array[i-2])
        return(fib_array[n])

n = int(input())
print(calc_fib(n))
