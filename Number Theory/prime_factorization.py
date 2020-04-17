# Prime Factors : Any of the prime numbers that can be multiplied to give the original number

# Question : Given number N, find it's prime factors
# Example  :
# 	        N = 12
# 	        Factors of 12 : 1,2,3,4,6,12
# 			simplifying   : 2,3,2,2,2,3 = > 2 = 4 times and 3 = 2 times => total = 6
# 			prime factors of 12 : 2*2*3  => (2**2) * (3**1) => 3*2 = 6

# ------------------| Brute Force Approach |-----------------

# Time Complexity : O(N)
def primeFact(n):
	ans = 1
	for i in range(2, n):
		if n % i == 0:
			cnt = 0
			while n % i == 0:
				cnt += 1
				n = n // i
			ans = ans * (cnt + 1)
	return ans


print(primeFact(12))


# ------------------| Optimized Approach |-----------------

# Time Complexity : O(sqrt(N)
def primeFact(n):
	cnt = 0
	ans = 1
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			cnt = 0
			while n % i == 0:
				cnt += 1
				n = n // i
			ans = ans * (cnt + 1)
	if n > 1:
		cnt += 1
		ans = ans * (cnt + 1)
	return ans


print(primeFact(100))


# --------------------------------| Short code |--------------------------------------

# Time Complexity : 0(sqrt(N))
# count number of prime factors
def cntFact(n):
	ct = 0
	for i in range(1, int(n ** 0.5) + 1):
		if n % i == 0:
			ct += 2
		if n == i ** 2:
			ct -= 1
	return ct


print(cntFact(4))

# -------------------------------| Short code to find Factors |---------------------------------

from functools import reduce


def factors(n):
	return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))
