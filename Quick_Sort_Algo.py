# Quick Sort is based on the concept of Divide and Conquer, just like merge sort
# 1. Select an element pivot from the array element
# 2. Rearrange the element in the array in such a way that all elements that
#    are less than the pivot appear before the pivot and all elements greater than the pivot element come after it.
# 3. After such a partitioning, the pivot is placed in it's final position.
# 4. Recursively sort the two sub-array.

# Worst Case Time Complexity [ Big-O ]: O(n2)
# Best Case Time Complexity [Big-omega]: O(n*log n)
# Average Time Complexity [Big-theta]: O(n*log n)
# Space Complexity: O(n*log n)


def partition(arr,start,end):
    pivot = arr[(start+end)//2]
    low = start - 1
    high = end + 1
    while True:
        low += 1
        while arr[low] < pivot:
            low += 1
        high -= 1
        while arr[high] > pivot:
            high -= 1
        if low >= high:
            return high
        # If an element at low (on the left of the pivot) is larger than the
        # element at high (on right right of the pivot), then swap them
        arr[low],arr[high] = arr[high],arr[low]

def quick_sort(arr):
    def _quick_sort(arr,start,end):
        if start < end:
            split_index = partition(arr,start,end)
            _quick_sort(arr,start,split_index)
            _quick_sort(arr,split_index+1,end)
    _quick_sort(arr,0,len(arr)-1)

arr = list(map(int,input().split()))
quick_sort(arr)
print(*arr)