#Uses python3

import sys
sys.setrecursionlimit(200000)

class DirectedGraph:
    def __init__(self, adj_graph):
        self.adj = adj_graph
        self.reverseGraph()
        self.reset()

    def reset(self):
        self.visited = [False] * len(self.adj)
        self.component_num = [0] * len(self.adj)
        self.preorder = [0] * len(self.adj)
        self.postorder = [0] * len(self.adj)
        self.clock = 0
        self.current_component_number = 0
    def previsit(self, index):
        self.clock += 1
        self.preorder[index] = self.clock
    def postvisit(self, index):
        self.clock += 1
        self.postorder[index] = self.clock
    def isConnected(self, x, y):
        self.reset()
        self.Explore(x)
        return self.visited[y]

    def DFS(self, reverse=False):
        self.reset()
        for v in range(len(self.visited)):
            if not self.visited[v]:
                self.Explore(v, reverse)

    def BFS(self, S):
        pass

    def Explore(self, v, reverse=False):
        self.visited[v] = True
        # print(v, self.visited, self.component_num)
        if not reverse:
            self.previsit(v)
            for edge in self.adj[v]:
                if not self.visited[edge]:
                    self.Explore(edge, reverse)
            self.postvisit(v)
        elif reverse:
            self.previsit(v)
            for edge in self.adj_reverse[v]:
                if not self.visited[edge]:
                    self.Explore(edge, reverse)
            self.postvisit(v)

    def SCCs(self): # get the strongly connected components
        self.DFS(reverse=True)
        postorder = self.postorder[:]
        postorder.sort(reverse=True)
        # print(self.adj, self.adj_reverse, self.postorder, self.preorder, postorder)
        self.visited = [False] * len(self.postorder)
        for i in postorder:
            index = self.postorder.index(i)
            # print(index, i)
            if not self.visited[index]:
                self.current_component_number += 1
                self.SCCExplore(index)

        return self.current_component_number


    def SCCExplore(self, v):
        self.visited[v] = True
        self.component_num = self.current_component_number
        for edge in self.adj[v]:
            if not self.visited[edge]:
                self.SCCExplore(edge)

    def reverseGraph(self):
        self.adj_reverse = [[] for _ in range(len(self.adj))]
        for i in range(len(self.adj)):
            item = self.adj[i]
            for j in item:
                self.adj_reverse[j].append(i)
# MY CODE ENDS HERE

def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here
    graph = DirectedGraph(adj)
    result = graph.SCCs()
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
