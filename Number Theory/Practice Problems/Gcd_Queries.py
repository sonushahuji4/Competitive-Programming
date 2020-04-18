# Problem Statement Link : https://www.codechef.com/problems/GCDQ

# Solution :

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)


for _ in range(int(input())):
	N, Q = map(int, input().split())
	arr = list(map(int, input().split()))
	prefix = [0] * (N + 1)
	suffix = [0] * (N + 2)

	for i in range(1, N + 1):
		prefix[i] = gcd(arr[i - 1], prefix[i - 1])

	for i in range(N, 0, -1):
		suffix[i] = gcd(arr[i - 1], suffix[i + 1])

	for _ in range(Q):
		L, R = map(int, input().split())
		ans = gcd(prefix[L - 1], suffix[R + 1])
		print(ans)
