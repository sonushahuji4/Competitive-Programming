# Problem Statement Link : https://www.spoj.com/problems/AMR11E/
arr = [0]
for n in range(30, 3000):
	temp = n
	cnt = 0
	result = set()
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			while n % i == 0:
				result.add(i)
				n = n // i
	if n > 1:
		result.add(n)
	if len(result) >= 3:
		arr.append(temp)

for _ in range(int(input())):
	n = int(input())
	print(arr[n])
