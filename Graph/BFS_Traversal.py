from collections import defaultdict
graph = defaultdict(list)
visited = []
queue = []

def addEdge(graph,u,v):
	graph[u].append(v)

def BFS(source):
	queue.append(source) # initially put source node in queue
	visited[source] = 1 # initially mark it visited
	while queue: # while queue is not empty
		s = queue.pop(0) # remove 1st element from the queue
		print(s,end=" ") # print ut
		for i in graph[s]: # get all the level wise nodes that are connected to current node
			if visited[i] == 0: # if it is not visited then
				queue.append(i) # put it in queue
				visited[i] = 1 # and mark it visited

n = int(input()) # number of nodes
visited = [0]*(n+1)
edge = int(input()) # number of edges that connects the nodes

for _ in range(edge):
	u,v = map(int,input().split())
	addEdge(graph,u,v) # would connect source and destination
	addEdge(graph,v,u) # would connect destination and source

source = int(input()) # starting traversal from
print(BFS(source))
print(graph) # check the connections
