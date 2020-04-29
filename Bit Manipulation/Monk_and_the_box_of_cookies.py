# Problem Statement Link : https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/monk-and-the-box-of-cookies/

for _ in range(int(input())):
	setBits = [0]*32
	for _ in range(int(input())):
		num = list(bin(int(input()))[2:])
		i = len(num)-1
		for lastDigit in num:
			if lastDigit == '1':
				setBits[i] += 1
			i -= 1
	max_ = max(setBits)
	print(setBits.index(max_))

