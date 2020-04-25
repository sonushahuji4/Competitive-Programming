# Reference Video Tutorial Link : https://www.youtube.com/watch?v=VNYkU1O3-0U
# Time Complexity = O(N)

def windowSlidingTechnique(arr, k, n):
	sum_ = max_ = 0
	for i in range(k):
		sum_ += arr[i]
	for i in range(1, n - k):
		sum_ = sum_ - arr[i - 1] + arr[i + k - 1]
		max_ = max(max_, sum_)
	return max_


arr = list(map(int, input().split()))
k = int(input())
print(windowSlidingTechnique(arr, k, len(arr)))
