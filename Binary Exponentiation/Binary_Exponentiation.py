# Video Reference Link : https://www.youtube.com/watch?v=-3Lt-EwR_Hw&t=1s
# Website Reference Link : https://cp-algorithms.com/algebra/binary-exp.html

# Binary exponentiation is a trick which allows to calculate an using only O(logn)
# multiplications (instead of O(n) multiplications required by the naive approach).

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