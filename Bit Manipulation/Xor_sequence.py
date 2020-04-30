# Problem Statement Link : https://www.hackerrank.com/challenges/xor-se/problem
def A(n):
	x = n % 8
	if x == 0 or x == 1: return n
	if x == 2 or x == 3: return 2
	if x == 4 or x == 5: return n + 2
	if x == 6 or x == 7: return 0
	return 0


for _ in range(int(input())):
	L, R = map(int, input().split())
	ans = A(R) ^ A(L-1)
	print(ans)
