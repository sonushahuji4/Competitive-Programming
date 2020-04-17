# Video Reference : https://www.youtube.com/watch?v=ga9N_ey4La4&list=PL2q4fbVm1Ik4liHX78IRslXzUr8z5QxsG&index=2

# Primality test is to determine whether the input interger is a prime or not

#    --------------------| Naive Approach |-------------------

# Time Complexity : O(n)
# Example:
# 	Input : 5       Output: True
# 	Input : 12      Output:  False

# Implementation
def isPrime(n):
	if n == 1:
		return False  # 1 is neither prime nor composite numbers
	for i in range(2, n):
		if n % i == 0:  # if any of i divides n then is not a prime number
			return False
	return True  # return True is number is prime


# print(isPrime(6))

# ---------------------------------------------------------------

#     ---------------------|  Better Approach  |-----------------

# Time Complexity : O(sqrt(n))
# All divisors of a number N occur in pairs of (a,b) .i.e (a * b) = N
# Example:
# 		12 has following divisors
# 		d = 1,2,3,4,6,12.
# 		paris are: (1,12),(2,6),(3,4)
# Claim: For a divisor pair(a,b) one of them lies below sqrt(N) and other lies above sqrt(N).

# Implementation
def isPrime(n):
	if n == 1:
		return False
	# loop runs till square root of n
	for i in range(2, int(n ** 0.5) + 1):  # u can use (i*i <= n) or (int(math.sqrt(n))+1)
		if n % i == 0:
			return False  # return False is number is not prime
	return True  # return True is number is prime

# print(isPrime(9))
