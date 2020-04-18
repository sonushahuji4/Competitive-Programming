# Problem Statement Link : https://www.hackerearth.com/practice/math/number-theory/primality-tests/practice-problems/algorithm/prime-interval/

# Solution 1 :

n = 100000

is_prime = [1 for _ in range(n)]
is_prime[0] = is_prime[1] = 0

for i in range(2, int(n ** 0.5) + 1):
	if is_prime[i]:
		for j in range(i * i, n, i):
			is_prime[j] = 0

L,R = map(int,input().split())
for i in range(L,R+1):
    if is_prime[i]:
        print(i,end=" ")

# Solution 2 :

def isPrime(n):
	if n == 1:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

L,R = map(int,input().split())
for i in range(L,R+1):
	if isPrime(i):
		print(i,end=" ")