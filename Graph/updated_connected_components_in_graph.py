from collections import defaultdict

graph = defaultdict(list)
visited = []

def addEdges(graph, u, v):
	graph[u].append(v)

def DFS(node):
	visited[node] = 1
	for data in graph[node]:
		if visited[data] == 0:
			DFS(data)

nodes, edges = map(int, input().split())
visited = [0] * (nodes + 1)
for _ in range(edges):
	u, v = map(int, input().split())
	addEdges(graph, u, v)
	addEdges(graph, v, u)

count_ = 0
for i in range(1, len(visited)):
	if visited[i] == 0:
		DFS(i)
		count_ += 1
print(count_)