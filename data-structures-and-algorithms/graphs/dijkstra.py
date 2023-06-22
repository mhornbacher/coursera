#Uses python3

import sys
import queue
import math


class DQueue:
    def __init__(self, dist):
        self.values = [i for i in dist]
        self.indexes = [i for i in range(len(dist))]
    def ExtractMin(self):
        index = self.values.index(min(self.values))
        return (self.values.pop(index), self.indexes.pop(index))
    def ChangePriority(self, node, value):
        self.values[self.indexes.index(node)] = value
    def empty(self):
        return len(self.values) <= 0

def Relax(edge, u, dist, prev, H):
    v = edge[0]
    w = edge[1]
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        prev[v] = u
        H.ChangePriority(v, dist[v])

def distance(adj, cost, s, t):
    #write your code here
    dist = [float('inf')] * len(adj)
    prev = [-1] * len(adj)

    dist[s] = 0
    H = DQueue(dist)
    while not H.empty():
        u = H.ExtractMin()[1]
        edges = list(zip(adj[u], cost[u]))
        for edge in edges:
            Relax(edge, u, dist, prev, H)
    if dist[t] == float('inf'):
        return -1
    return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
