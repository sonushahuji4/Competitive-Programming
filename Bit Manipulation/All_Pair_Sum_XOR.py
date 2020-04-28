# Reference Video Tutorial Link : https://www.youtube.com/watch?v=LyMPfMe7T58&list=PL2q4fbVm1Ik7ip1VkWwe5U_CEb93vw6Iu&index=6

def sum_(arr):
	ans = 0
	for i in range(len(arr)):
		ans += 2 * arr[i]
		for j in range(i + 1, len(arr)):
			ans += 2 * (arr[i] + arr[j])
	return ans


for _ in range(int(input())):
	arr = list(map(int, input().split()))
	print(sum_(arr))
