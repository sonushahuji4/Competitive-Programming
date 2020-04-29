# Reference Video Tutorial Link : https://www.youtube.com/watch?v=_o7QBzM33J0&list=PL2q4fbVm1Ik7ip1VkWwe5U_CEb93vw6Iu&index=4

# Given : A number N and find number of set(1's) bits in it.

# ------------------------------------------------------| Approach  1 |------------------------------------------------------

# Example :
# 			N = 12 => (1 1 0 0)  => OUTPUT : 2
# 			N = 11 => (1 0 1 1)  => OUTPUT : 3
#
# Solution :  We will be using right shift to find total set not bits
#
# 			N = 0 1 0 0 1 1 1 0
#
# OPERATIONS : (and bit operation)    N & 1
#
# 				0 1 0 0 1 1 1 0
# 				0 0 0 0 0 0 0 1
# 			-----------------------
# 				0 0 0 0 0 0 0 0     here : 0 & 1 = 0, so we do not increment count
# 			-----------------------
#
# 			: (Right shift operation) N >> 1
#
# 			N = 0 0 1 0 0 1 1 1
#
# 				0 0 1 0 0 1 1 1
# 				0 0 0 0 0 0 0 1
# 			-----------------------
# 				0 0 0 0 0 0 0 1     here : 0 & 1 = 1, so we increament count by 1
# 			-----------------------
# Repeat until N becomes 0

# Time Complexity : O(Log(N))
for _ in range(int(input())):
	n = int(input())
	ans = 0
	while n > 0:
		if (n & 1) > 0:
			ans += 1
		n = n >> 1  # at some point n becomes zero,
	print(ans)

# ------------------------------------------------------| Approach  2 |------------------------------------------------------

# Observation :
# 				8 - 1 = 7
#
# 			8 ==>     0 1 0 0 0     here => when u subtract N - 1, in binary representation  after 1, it makes all number 1's
# 			1 ==>     0 0 0 0 1
# 					-
# 					--------------
# 					   0 0 1 1 1    <== after subtracting N - 1
# 					--------------
# 			similary
#
# 			16 - 1 = 15
#
# 			16 ==>     1 0 0 0 0     here => when u subtract N - 1, in binary representation  after 1, it makes all number 1's
# 			1  ==>     0 0 0 0 1
# 					-
# 					--------------
# 					   0 1 1 1 1    <== after subtracting N - 1
# 					--------------

# Time Complexity : O(Log(N))

for _ in range(int(input())):
	n = int(input())
	ans = 0
	while n > 0:
		ans += 1
		n = n & (n - 1)
	print(ans)
