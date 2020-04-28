# Problem Statement Link : https://www.hackerrank.com/challenges/lonely-integer/problem

n = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(n):
	ans = ans ^ arr[i]
print(ans)
