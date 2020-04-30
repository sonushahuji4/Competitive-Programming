# Problem Statement Link : https://www.hackerrank.com/challenges/sum-vs-xor/problem
n = int(input())
ans = 1
while n > 0:
	if n % 2 == 0:
		ans *= 2
	n = n // 2
print(ans)
