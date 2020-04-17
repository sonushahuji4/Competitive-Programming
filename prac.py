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

graph = defaultdict(list)
graph[1].append(2)
graph[1].append(3)
graph[2].append(4)
graph[2].append(5)