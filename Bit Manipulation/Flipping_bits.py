# Problem Statement Link : https://www.hackerrank.com/challenges/flipping-bits/problem

# ---------------------------------------| Approach One |---------------------------------------
for _ in range(int(input())):
	n = bin(int(input()))[2:]
	n = list(n.zfill(32))
	st = ""
	for i in range(32):
		if n[i] == '0':
			st += '1'
		else:
			st += '0'
	print(int(st, 2))

# ---------------------------------------| Approach Two |---------------------------------------

for _ in range(int(input())):
    n = int(input())
    print(n^(2**32-1))
