from collections import defaultdict

def ConnectNodes(graph,u,v):
	graph[u].append(v)
	graph[v].append(u)

for _ in range(int(input())): # Nos. of test cases
	n = int(input()) # Nos. of nodes
	graph = defaultdict(list) # this is to store nodes and all connections to u to v
	for _ in range(n-1): # n-1 connections
		u,v = map(int,input().split())
		ConnectNodes(graph,u,v)

	query = int(input()) # Nos. of query
	for _ in range(query):
		u,v = map(int,input().split())
