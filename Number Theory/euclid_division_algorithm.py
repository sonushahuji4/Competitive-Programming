# Video Reference Link : https://www.youtube.com/watch?v=WHVKkc8zSH4&list=PL2q4fbVm1Ik4liHX78IRslXzUr8z5QxsG&index=14

# --------------------| Euclid Division Lemma |--------------------

# For positive integers A and B,there exist integer "q" (quotient) and "r" (remainder)
# such that :
#           Formula : Dividend = Divisor * Quotient + Remainder
#						D       = d       *  q       +  r
# 			D = d*q + r     where  0 <= r < d   # remainder is always smaller than divisor


# --------------------| Understanding Modular Arithmetic |--------------------
# Important :
# 				1) (N1 + N2) % mod = ((N1 % mod) + (N2 % mod)) % mod
#               2) (N1 - N2) % mod = ((N1 % mod) - (N2 % mod)) % mod
#               3) (N1*N2) % mod = ((N1 % mod) * (N2 % mod)) % mod
#               4)


# --------------------| Euclid Division Algorithm |--------------------
# Important : "b" always has to be greater than "a".
# 							a,          if b = 0
# 				gcd(a,b) =
# 	            			gcd(b,a mod b), otherwise
# Example : Find GCD(140,12)
#           GCD(140,12)
#           GCD(12,8)
#           GCD(8,4)
#           GCD(4,0) so answer is 4


def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)


print(gcd(140, 12))

# ---------------------| Important Property of GCD |--------------------
# Let GCD of A and B = g
# Observation 1 : GCD(A,0) = GCD(0,A) = A
# Observation 2 : GCD(A,B) = GCD(B,A)
# Observation 3 : GCD(A,B) = GCD(A-B,B) = GCD(A,B-A)