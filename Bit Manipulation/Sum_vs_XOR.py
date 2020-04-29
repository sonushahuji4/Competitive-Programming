# Problem Statement Link : https://www.hackerrank.com/challenges/sum-vs-xor/problem
n = int(input())
ans = 0
for i in range(n):
	if n + i == n ^ i:
		ans += 1
print(ans)
