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