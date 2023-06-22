#Uses python3

import sys

# MY CODE STARTS HERE
class Graph:
    def __init__(self, adj_graph):
        self.adj = adj_graph
        self.reset()
    def reset(self):
        self.visited = [False] * len(self.adj)
    def isConnected(self, x, y):
        self.reset()
        self.Explore(x)
        return self.visited[y]
    def Explore(self, v):
        self.visited[v] = True
        for edge in self.adj[v]:
            if not self.visited[edge]:
                self.Explore(edge)
    
# MY CODE ENDS HERE

def reach(adj, x, y):
    #write your code here
    graph = Graph(adj)
    if graph.isConnected(x, y):
        return 1
    return 0

if __name__ == '__main__':
    given_input = sys.stdin.read()
    data = list(map(int, given_input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
