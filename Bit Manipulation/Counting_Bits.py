# Problem Statement Link : https://leetcode.com/problems/counting-bits/

n = int(input())
setBits = []
for i in range(n+1):
	ans = 0
	while i > 0:
		ans += 1
		i = i & (i - 1)
	setBits.append(ans)
print(setBits)
