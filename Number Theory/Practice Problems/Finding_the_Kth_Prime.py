# Problem Statement Link : https://www.spoj.com/problems/TDKPRIME/
n = 50000000

is_prime = [True for _ in range(n)]
is_prime[0] = is_prime[1] = 0

for i in range(2, int(n ** 0.5) + 1):
	if is_prime[i]:
		for j in range(i * i, n, i):
			is_prime[j] = 0

prime_list = []
for i in range(len(is_prime)):
	if is_prime[i]:
		prime_list.append(i)

for _ in range(int(input())):
	num = int(input())
	print(prime_list[num-1])