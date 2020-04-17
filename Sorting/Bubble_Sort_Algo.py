# Explanation
# Bubble sort, sorts the array elements by repeatedly moving the largest element to the highest index position.
# In bubble sorting, consecutive adjacent pairs of elements in the array are compared with each other.
# If the element at the lower index is greater than the element at the higher index then the two elements are interchanged
# so that the element is placed before the bigger one.
# NOTE: At the end of first pass, the largest element in the arr will be placed it's proper position

# Worst Case Time Complexity [ Big-O ]: O(n2)
# Best Case Time Complexity [Big-omega]: O(n)
# Average Time Complexity [Big-theta]: O(n2)
# Space Complexity: O(1)

arr = list(map(int,input().split()))
n = len(arr)
status = False
for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1], arr[j]
            status = True
    if status == False: # if the arr is already sorted then break
        break
print(*arr)
