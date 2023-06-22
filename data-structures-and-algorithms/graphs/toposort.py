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
        self.order = []
        self.current_component_number = 0
    def previsit(self, index):
        self.clock += 1
        self.previsit_clock[index] = self.clock
    def postvisit(self, index):
        self.clock += 1
        self.postvisit_clock[index] = self.clock
        self.order.append(index)
    def DFS(self):
        self.reset()
        for v in range(len(self.visited)):
            if not self.visited[v]:
                self.current_component_number += 1
                self.Explore(v)

    def Explore(self, v):
        self.visited[v] = True
        # print(v, self.visited, self.component_num)
        self.previsit(v)
        for edge in self.adj[v]:
            if not self.visited[edge]:
                self.Explore(edge)
        self.postvisit(v)

    def getTopologicalOrder(self):
        self.DFS()
        return reversed(self.order) # We need to go from front to back and not back to front ;-) so reverse
# MY CODE ENDS HERE


def dfs(adj, used, order, x):
    #write your code here
    pass


def toposort(adj):
    # used = [0] * len(adj)
    # order = []
    #write your code here
    graph = DirectedGraph(adj)
    return graph.getTopologicalOrder()
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

