# Video Reference Link 1 : https://www.youtube.com/watch?v=-3Lt-EwR_Hw&t=1s
# Video Reference Link 2 : https://www.youtube.com/watch?v=8nOaPV-o5Pg&list=PL2q4fbVm1Ik4liHX78IRslXzUr8z5QxsG&index=7
# Website Reference Link : https://cp-algorithms.com/algebra/binary-exp.html

# Binary exponentiation is a trick which allows to calculate a**n using only O(logN)
# multiplications (instead of O(n) multiplications required by the naive approach).

# --------------------------| Brute Force Approach |-------------------------------

# Time Complexity : O(N)
def power(base, expo):
	ans = 1
	for i in range(expo):
		ans = ans * base
	return ans


print(power(2, 12))


# --------------------------| Optimizes Approach |-------------------------------
# Time Complexity : O(log(N))
def power(base, expo):
	ans = 1
	while expo:  # expo is not zero, iterate
		if expo & 1 == 1:  # if number is odd
			ans = ans * base
			expo -= 1
		base = base * base
		expo = expo // 2
	return ans


print(power(2, 13))

# --------------------------| Modular Optimizes Approach |-------------------------------
# Time Complexity : O(log(N))
def power(base, expo,mod):
	ans = 1
	while expo:  # expo is not zero, iterate
		if expo & 1 == 1:  # if number is odd
			ans = (ans * base)% mod
			expo -= 1
		base = (base * base) % mod
		expo = expo // 2
	return ans


print(power(2, 13,mod = 10**9+7))

# ------------------------------| Different Approach |-----------------------------

# Time Complexity : O(log(N))
# Recursive Approach
def power(a,n):
	if n == 0:
		return 1
	elif n == a:
		return a
	else:
		R = power(a,n//2)
		if n%2 == 0:
			return R*R
		else:
			return R*a*R

#........................................
# Time Complexity : O(log(N))
# Iterative Approach
def binpow(a,n,m = 10**9+7):
	res = 1
	a %= m
	while n > 0:
		if n&1: # if number is even then
			res = res * a%m
		a = a * a%m
		n >>= 1 # shift 1 bit to right
	return res