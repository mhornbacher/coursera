#Uses python3

import sys

# MY CODE STARTS HERE
class DirectedGraph:
    def __init__(self, adj_graph):
        self.adj = adj_graph
        self.reset()
    def reset(self):
        self.visited = [False] * len(self.adj)
        self.component_num = [0] * len(self.adj)
        self.previsit_clock = [0] * len(self.adj)
        self.postvisit_clock = [0] * len(self.adj)
        self.clock = 0
        self.current_component_number = 0
    def previsit(self, index):
        self.clock += 1
        self.previsit_clock[index] = self.clock
    def postvisit(self, index):
        self.clock += 1
        self.postvisit_clock[index] = self.clock
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
        self.previsit(v)
        self.component_num[v] = self.current_component_number
        # print(v, self.visited, self.component_num)
        for edge in self.adj[v]:
            if not self.visited[edge]:
                self.Explore(edge)
        self.postvisit(v)
    def totalComponents(self):
        self.DFS()
        return self.current_component_number

    def isAcyclic(self):
        self.DFS()
        for vertex_index in range(len(self.adj)):
            vertex_post = self.postvisit_clock[vertex_index]
            for edge in self.adj[vertex_index]:
                if vertex_post < self.postvisit_clock[edge]:
                    return False
        return True
# MY CODE ENDS HERE

def acyclic(adj):
    graph = DirectedGraph(adj)
    if not graph.isAcyclic():
        return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
