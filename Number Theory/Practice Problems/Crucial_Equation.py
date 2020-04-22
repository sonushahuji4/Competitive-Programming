# Problem Statement Link : https://www.spoj.com/problems/CEQU/
def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)


for i in range(int(input())):
	a, b, c = map(int, input().split())
	ans = "No"
	if c % gcd(a, b) == 0:
		ans = "Yes"
	print("{} {}: {}".format("Case", (i + 1), ans))