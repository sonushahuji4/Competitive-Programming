# Problem : https://www.codechef.com/problems/PRB01

# Solution

def isPrime(n):
	if n == 1:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True


for _ in range(int(input())):
	n = int(input())
	ans = "yes"
	if isPrime(n) == False:
		ans = "no"
	print(ans)