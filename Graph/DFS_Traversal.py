from collections import defaultdict
graph = defaultdict(list)
visited = []
stack = []

def addEdge(graph,u,v):
	graph[u].append(v)

def DFS(source):
	stack.insert(0,source) # initially put source node in stack
	visited[source] = 1 # initially mark it visited
	while stack: # while stack is not empty
		s = stack.pop() # remove last element from the stack
		print(s,end=" ") # print it
		for i in graph[s]:
			if visited[i] == 0: # if it is not visited then
				visited[i] = 1  # mark it visited
				stack.insert(0,i) # and put it in stack
nodes = int(input()) # number of nodes
visited = [0]*(nodes+1)
edges = int(input()) # number of edges that connects the nodes

for _ in range(edges):
	u,v = map(int,input().split())
	addEdge(graph,u,v) # would connect source and destination
	addEdge(graph,v,u) # would connect destination and source

source = int(input()) # starting node
print(DFS(source))
