# Video Reference : https://www.youtube.com/watch?v=yCxV0kBpA6M
# Explanation
# The array of values to be sorted is divided into two sets
# 1) one that stores sorted values and
# 2) another that contains unsorted values
# The sorting algo will proceed until there are elements in the unsorted set.
# Suppose there are n elements in the array, Initially, the element with index zero is in the sorted set
# and rest of the elements are in the unsorted set
# The first element if the unsorted partition has array index 1
# During each iteration of the algorithm, the 1st element in the unsorted set is picked up and inserted into correct position in the sorted set.

# If we provide an already sorted array to the insertion sort algorithm,
# it will still execute the outer for loop, thereby requiring n steps to sort an already sorted array of n elements,
# which makes its best case time complexity a linear function of n.

# Worst Case Time Complexity [ Big-O ]: O(n2)
# Best Case Time Complexity [Big-omega]: O(n)
# Average Time Complexity [Big-theta]: O(n2)
# Space Complexity: O(1)

arr = list(map(int, input().split()))
n = len(arr)
for i in range(1, n):
	item_to_insert = arr[i]  # pick one value from unsorted arr
	j = i - 1  # keep trak of last index of sorted arr
	while j >= 0 and arr[j] > item_to_insert:  # compare item_to_insert with sorted arr
		arr[j + 1] = arr[j]  # then insert at it's proper position in sorted arr
		j = j - 1
	arr[j + 1] = item_to_insert
print(*arr)
