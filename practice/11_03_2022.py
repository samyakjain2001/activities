#BINARY SEARCH
# Aim is to compare time complexity of binary search and naive search

import random
import time
def naiveSearch(arr, target):
    for i in range(len(arr)):
        if(arr[i]==target):
            return i;

def binarySearch(arr, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1
    
    mid = (low+high) // 2
    while(arr[mid] != target):
        if(arr[mid] == target):
            return mid
        if(arr[mid] > target):
            return binarySearch(arr, target, mid + 1, high)
        else:
            return binarySearch(arr, target, low, mid - 1)
    
if __name__=='__main__':
    length = 10000
    #build a sorted list of length 10000
    sorted_list = set()
    while (len(sorted_list) < length):
        sorted_list.add(random.randint(-3*length, 3*length))

    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naiveSearch(sorted_list, target)
    end = time.time()
    print("\nNaive Search time: ", ((end - start)/length) * 1000,"milli-seconds")
    start = time.time()
    for target in sorted_list:
        binarySearch(sorted_list, target)
    end = time.time()
    print("Binary Search time: ", ((end - start)/length) * 1000,"milli-seconds")