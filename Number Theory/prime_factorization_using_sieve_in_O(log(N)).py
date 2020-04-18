# Video Reference Link 1 : https://www.youtube.com/watch?v=DQJfvz2Dhss&list=PL2q4fbVm1Ik4liHX78IRslXzUr8z5QxsG&index=10
# Video Reference Link 2 : https://www.youtube.com/watch?v=kQr-ezPWgWM

# Time Complexity : O(log(N))

from collections import Counter

primeFactors = [0 for _ in range(10001)]


def primeFactorizationUsingSieve(n):
	for i in range(2, int(n ** 0.5) + 1):
		if not primeFactors[i]:
			primeFactors[i] = i
			for j in range(i * i, n, i):
				primeFactors[j] = i
	return primeFactors


primeFactorizationUsingSieve(10001)

for _ in range(int(input())):
	num = int(input())
	pri_fact = []
	while primeFactors[num] != 0 and primeFactors[num] > 0:
		pri_fact.append(primeFactors[num])
		num = num // primeFactors[num]
	print(Counter(pri_fact))
