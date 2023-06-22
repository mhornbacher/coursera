# Uses python3
import sys
from math import ceil, floor

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

def myWay(a):
    if len(a) == 1:
        return 1
    a.sort()
    previous = -100
    min_amount = floor(len(a)/2)
    for i in range(0, min_amount + 1):
        if a[i] != previous:
            previous = a[i]
            if i + min_amount > len(a) - 1:
                return 0
            if a[i + min_amount] == a[i]:
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # if get_majority_element(a, 0, n) != -1:
    #     print(1)
    # else:
    #     print(0)
    print(myWay(a))

def test(n_scale, array_base):
    import random
    while True:
        amount_of_numbers = random.randint(1, 10**n_scale)
        numbers = []
        majority = bool(random.getrandbits(1))
        if majority:
            answer = random.randint(1, 10**array_base)
            for i in range(0, int(amount_of_numbers) // 2 + 1):
                numbers.append(answer)
            for i in range(0, amount_of_numbers // 2 - 1):
                numbers.append(random.randint(1, 10**array_base))
            random.shuffle(numbers)
            print(numbers)
            result = myWay(numbers)
            print(result)
            if result != 1:
                print("ERROR", result, answer, numbers)
                break
        else:
            for i in range(0, amount_of_numbers):
                numbers.append(random.randint(1, 10**array_base))
            random.shuffle(numbers)
            print(numbers)
            result = myWay(numbers)
            print(result)
            if result != 0 and len(numbers) > 1:
                print("ERROR", result, majority, numbers)
                break
            
