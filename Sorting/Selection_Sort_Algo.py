# Video Reference : https://www.youtube.com/watch?v=9oWd4VJOwr0
# Explanation:
# First find the smallest element in the array and place it in the first position.
# Then, find the second smallest element in the array and place it in the second position.
# Repeat this procedure until the entire array is sorted

# Worst Case Time Complexity [ Big-O ]: O(n2)
# Best Case Time Complexity [Big-omega]: O(n2)
# Average Time Complexity [Big-theta]: O(n2)
# Space Complexity: O(1)

arr = list(map(int, input().split()))
n = len(arr)
for i in range(n):
	lowest_value_index = i  # consider 1st value is smallest then all
	for j in range(i + 1, n):
		if arr[j] < arr[lowest_value_index]:
			lowest_value_index = j
	arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]
print(*arr)
