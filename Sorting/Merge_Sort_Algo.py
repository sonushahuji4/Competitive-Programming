# Video Reference : https://www.youtube.com/watch?v=jlHkDBEumP0&t=502s
# If we can break a single big problem into smaller sub-problems,
# solve the smaller sub-problems and combine their solutions to find the solution for the original big problem,
# it becomes easier to solve the whole problem.

# Explanation:
# A divide-and-conquer algorithm works by recursively breaking down a large problem into two or more sub-problems of the same or related type,
# until these become small enough to be solved directly.
# The solutions to the sub-problems are then combined to give a solution to the original problem.

# If the array contains one element, then it is already sorted
# Otherwise, divide the unsorted array into two sub-array of about half the size.
# Use merge sort algo recursively to sort each sub-array
# Merge the two sub-array to form a single sorted array

# Worst Case Time Complexity [ Big-O ]: O(n*log n)
# Best Case Time Complexity [Big-omega]: O(n*log n)
# Average Time Complexity [Big-theta]: O(n*log n)
# Space Complexity: O(n)

def merge(left_sub_arr,right_sub_arr):
    sorted_arr = []
    left_index = right_index = 0
    left_arr_length, right_arr_length = len(left_sub_arr),len(right_sub_arr)
    for _ in range(left_arr_length+right_arr_length):
        if left_index < left_arr_length and right_index < right_arr_length:
            if left_sub_arr[left_index] <= right_sub_arr[right_index]:
                sorted_arr.append(left_sub_arr[left_index])
                left_index += 1
            else:
                sorted_arr.append((right_sub_arr[right_index]))
                right_index += 1
        elif left_index == left_arr_length:
            sorted_arr.append((right_sub_arr[right_index]))
            right_index += 1
        elif right_index == right_arr_length:
            sorted_arr.append((left_sub_arr[left_index]))
            left_index += 1
    return sorted_arr

def merge_sort(arr):
    if len(arr) <= 1:  # if there is one element in arr then it means, it is already sorted
        return arr  # simply return the arr
    mid = len(arr) // 2  # divide arr into two equal array
    left_sub_arr = merge_sort(arr[:mid])
    right_sub_arr = merge_sort(arr[mid:])
    return merge(left_sub_arr,right_sub_arr)

arr = list(map(int,input().split()))
list_ = merge_sort(arr)
print(list_)