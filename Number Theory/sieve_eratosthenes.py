# ------------------| Sieve Of Eratosthenes Algo for finding prime numbers |--------------------------------------
# Time Complexity : Nlog(log(N))
# 0 => represents composite number
# 1 => represents prime number
n = 15
is_prime = [1 for i in range(n)]
is_prime[0] = is_prime[1] = 0

for i in range(2,int(n**0.5)+1):
	if is_prime[i]:
		for j in range(i*i,n,i):
			is_prime[j] = 0
print(*is_prime)