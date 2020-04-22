# Problem Statement Link : https://www.spoj.com/problems/DIVSUM/

# Solution :


for _ in range(int(input())):
	n = int(input())
	ans = 0
	i = 1
	while i * i < n:
		if n % i == 0:
			ans += i + n // i
		i += 1
	if i * i == n:
		ans += i
	print(ans - n)
