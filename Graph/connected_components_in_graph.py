from collections import defaultdict
graph = defaultdict(list)
visited = []

def addEdges(graph,u,v):
	graph[u].append(v)

def connected_components():
	count_ = 0
	for i in range(1,len(visited)):
		if visited[i] == 0:
			DFS(i)
			count_ += 1
	print()
	print(count_)

def DFS(s):
	visited[s] = 1
	print(s,end=" ")
	for data in graph[s]:
		if visited[data] == 0:
			DFS(data)

nodes = int(input())
visited = [0]*(nodes+1)
edges = int(input())
for _ in range(edges):
	u,v = map(int,input().split())
	addEdges(graph,u,v)
	addEdges(graph,v,u)

connected_components()
