#Uses python3

import sys

# MY CODE STARTS HERE
class Graph:
    def __init__(self, adj_graph):
        self.adj = adj_graph
        self.reset()
    def reset(self):
        self.visited = [False] * len(self.adj)
        self.component_num = [0] * len(self.adj)
        self.current_component_number = 0
    def isConnected(self, x, y):
        self.reset()
        self.Explore(x)
        return self.visited[y]
    def DFS(self):
        self.reset()
        for v in range(len(self.visited)):
            if not self.visited[v]:
                self.current_component_number += 1
                self.Explore(v)
    def Explore(self, v):
        self.visited[v] = True
        self.component_num[v] = self.current_component_number
        # print(v, self.visited, self.component_num)
        for edge in self.adj[v]:
            if not self.visited[edge]:
                self.Explore(edge)
    def totalComponents(self):
        self.DFS()
        return self.current_component_number
    
# MY CODE ENDS HERE

def number_of_components(adj):
    result = 0
    #write your code here
    graph = Graph(adj)
    result = graph.totalComponents()
    return result

if __name__ == '__main__':
    given_input = sys.stdin.read()
    data = list(map(int, given_input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
