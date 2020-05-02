# Problem Statement Link : https://www.hackerrank.com/challenges/and-product/problem
for _ in range(int(input())):
	a, b = map(int, input().split())
	ans = a
	for i in range(a+1, b):
		ans = ans*a
	print(ans)
