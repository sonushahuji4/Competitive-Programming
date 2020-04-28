# Reference Video Tutorial Link : https://www.youtube.com/watch?v=IO2D1g2QP6E&list=PL2q4fbVm1Ik7ip1VkWwe5U_CEb93vw6Iu&index=3

# Given a number N and index i, find whether ith bits in binary representation of N is set(1) or not(0).
# Solutions
# N = 12
# Binary Representation of 12 = 0 0 0 0 1 1 0 0       <= do not perform left shift on this number.
# Let num = 1
# Binary Representation of 1 = 0 0 0 0 0 0 0 1        <= do left shift on this number ith times
#
# Now perform and "&" operation:

for _ in range(int(input())):
	N = int(input())
	ith = int(input())
	num = 1
	num = num << ith
	ans = num & N
	if ans == 0:
		print("NOT SET")
	else:
		print("SET")
