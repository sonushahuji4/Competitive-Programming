# Problem Statement Link : https://leetcode.com/problems/number-of-1-bits/#

num = int(input())
ans = 0
while num:
	ans += 1
	num = num & (num - 1)
print(ans)
