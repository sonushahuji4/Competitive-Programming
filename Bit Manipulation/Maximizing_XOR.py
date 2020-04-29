# Problem Statement Link : https://www.hackerrank.com/challenges/maximizing-xor/problem

L = int(input())
R = int(input())
max_ = -1000000007
for i in range(L, R + 1):
	for j in range(i + 1, R + 1):
		ans = i ^ j
		max_ = max(max_, ans)
print(max_)
