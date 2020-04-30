# Problem Statement Link : https://www.hackerrank.com/challenges/counter-game/problem

for _ in range(int(input())):
	n = int(input())
	n = n - 1
	ans = 0
	while n > 0:
		if n & 1 == 1:
			ans += 1
		n = n >> 1
	if ans & 1 == 0:
		print("Richard")
	else:
		print("Louise")
