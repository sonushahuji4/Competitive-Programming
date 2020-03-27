n,x,y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
li = []
for i in range(n):
	if A[i] >= B[i]:
		li.append([abs(A[i]-B[i]),1,i])
	else:
		li.append([abs(A[i] - B[i]), 0, i])
li.sort(reverse=True)
x_ = y_ = ans = 0
for data in li:
	if (x_+1 <= x) and data[1] == 1:
		x_ += 1
		ans += A[data[2]]
	elif (y_+1 <= y):
		y_ += 1
		ans += B[data[2]]
print(ans)