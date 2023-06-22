# Uses python3
import sys
import random

def partition3(a):
    pivot_item = a[0]    # the pivot is the left most item to partition
    less, equal, greater = [], [], [] #create 3 arrays. 1 for less then one for equal and one for greater
    for item in a:
        if item < pivot_item: less.append(item)
        elif item == pivot_item: equal.append(item)
        elif item > pivot_item: greater.append(item)
    
    return less, equal, greater

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort_3(a):
    if len(a) <= 1:
        return a
    k = random.randint(0, len(a) - 1) # Apparently in python random is the same as len
    a[0], a[k] = a[k], a[0] # swap the random pick with the first item
    less, equal, greater = partition3(a) # get all the parts
    return randomized_quick_sort_3(less) + equal + randomized_quick_sort_3(greater) # run recursively
    
# for god knows what reason python is doing some weird mix of pass by refrence and pass by value. this code is as such trash
def randomized_quick_sort(a, l, r):
    if l >= r:
        return a
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);

    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a = randomized_quick_sort_3(a)
    for x in a:
        print(x, end=' ')

