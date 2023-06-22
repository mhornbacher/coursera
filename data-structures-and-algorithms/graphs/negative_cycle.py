#Uses python3

import sys
# from IPython import embed


def Relax(u, edge, dist, prev):
    v = edge[0]
    w = edge[1]
    res = False
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        prev[v] = u
        res = True
    return res


def negative_cycle(adj, cost):
    #write your code here
    prev = [-1] * len(adj)
    dist = [float('inf')] * len(adj)
    dist[0] = 0
    for i in range(len(adj) - 1):
        for u in range(len(adj)):
            if dist[u] == float('inf'):
                dist[u] = 0 # set it to a start if we have not hit it yet
            edges = list(zip(adj[u], cost[u]))
            for edge in edges:
                Relax(u, edge, dist, prev)
    res = 0
    for u in range(len(adj)):
            edges = list(zip(adj[u], cost[u]))
            for edge in edges:
                if Relax(u, edge, dist, prev):
                    res = 1
    # embed()
    return res


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
    print(negative_cycle(adj, cost))
