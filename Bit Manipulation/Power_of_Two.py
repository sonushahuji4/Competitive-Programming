# Problem Statement Link : https://leetcode.com/problems/power-of-two/

def powerOfTwo(n):
	if n < 0: return False
	ans = 0
	while n:
		ans += 1
		n = n & (n - 1)
	if ans == 1:
		return True
	else:
		return False


n = int(input())
print(powerOfTwo(n))
