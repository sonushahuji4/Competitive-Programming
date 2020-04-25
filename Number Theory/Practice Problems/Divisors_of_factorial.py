# Problem Statement Link :  https://www.spoj.com/problems/DIVFACT/
from collections import Counter

primeFactors = [0 for _ in range(50000)]


def primeFactorizationUsingSieve(n):
	for i in range(2, int(n ** 0.5) + 1):
		if not primeFactors[i]:
			primeFactors[i] = i
			for j in range(i * i, n, i):
				primeFactors[j] = i
	return primeFactors


primeFactorizationUsingSieve(50000)
modulo = 1000000007
for _ in range(int(input())):
	num = int(input())
	temp = num
	pri_fact = []
	while temp > 0:
		num = temp
		while primeFactors[num] != 0 and primeFactors[num] > 0:
			pri_fact.append(primeFactors[num])
			num = num // primeFactors[num]
		temp -= 1
	data = Counter(pri_fact)
	ans = 1
	for d in data.values():
		ans = ((ans % modulo) * ((d + 1) % modulo)) % modulo
	print(ans)
