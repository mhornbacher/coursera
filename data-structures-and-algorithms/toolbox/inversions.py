# Uses python3
import sys

def mergeSort(array):
    number_of_inversions = 0
    if len(array) <= 1:
        print("bottom level", array)
        return number_of_inversions, array
    
    midpoint = (0 + len(array)) // 2
    
    inversions1, array1 = mergeSort(array[:midpoint])
    inversions2, array2 = mergeSort(array[midpoint:])
    
    internalinversions, finalArray = merge(array1, array2)

    number_of_inversions = internalinversions + inversions1 + inversions2
    
    return number_of_inversions, finalArray

def merge(array1, array2):
    print("merged ", array1, array2, " -> ", end=' ')
    result = []
    inversions = 0
    while len(array1) > 0 or len(array2) > 0:
        if len(array1) == 0:
            result += array2
            break
        elif len(array2) == 0:
            result += array1
            inversions += len(array1)
            print("Inversion final -> ", inversions, end=' ')
            break
        if array1[0] <= array2[0]:
            result.append(array1.pop(0))
        else:
            result.append(array2.pop(0))
            inversions += 1
            print("Inversion -> ", inversions, end=' ')
    print("\nresult: ", array1, array2, " -> ", result)
    return inversions, result

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    inversions, sorted_array = mergeSort(a)
    print(inversions, sorted_array)
