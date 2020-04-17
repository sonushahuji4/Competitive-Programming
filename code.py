import math
from collections import defaultdict
from collections import Counter

modulo = 1000000007

def bfs(graph, source, dest):
    queue = [[source]]
    visited = set()
    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        if vertex == dest:
            return path
        elif vertex not in visited:
            for adj in graph.get(vertex, []):
                new_path = list(path)
                new_path.append(adj)
                queue.append(new_path)
            visited.add(vertex)

for _ in range(int(input())):
	graph = defaultdict(list)
	n = int(input())

	for _ in range(n - 1):
		u, v = map(int, input().split())
		graph[u].append(v)
		graph[v].append(u)

	arr = defaultdict(list)
	cost = list(map(int, input().split()))
	for k in range(n):
		temp = cost[k]
		# find prime factors of each number
		while temp % 2 == 0:
			arr[k + 1].append(2)
			temp = temp // 2
		for i in range(3, int(math.sqrt(temp)) + 1, 2):
			while temp % i == 0:
				arr[k + 1].append(i)
				temp = temp // i
		if temp > 2:
			arr[k + 1].append(temp)

	for _ in range(int(input())):
		source, goal = map(int, input().split())
		num = 1
		data = bfs(graph, source, goal)

		# merger specific list to one list
		merge_ = []
		for i in data:
			merge_  += arr[i]
		x = Counter(merge_) # get count of each number

		ans = 1
		for c in x:
			ans = (x[c]+1)*ans
		print(ans)
