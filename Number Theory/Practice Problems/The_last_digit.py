# Problem Link : https://www.spoj.com/problems/LASTDIG/

# Solution :

for _ in range(int(input())):
	a, b = map(int, input().split())
	if a == 0 and b > 0:
		print(0)
	elif a > 0 and b == 0:
		print(1)
	else:
		ans = 0
		if b % 4 == 0:
			rem = 4
		else:
			rem = b % 4
		ans = pow(a, rem, 1000000007)
		print(ans % 10)
