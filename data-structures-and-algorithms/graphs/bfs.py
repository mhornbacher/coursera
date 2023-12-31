#Uses python3

import sys
import queue
import math

# def distance(adj, s, t):
#     #write your code here
#     return -1

def distance(adj, s, t):
    distance = [-1] * len(adj)

    distance[s] = 0
    queue = [s]
    while len(queue) > 0:
        node_index = queue.pop(0) # pull from the front
        for edge in adj[node_index]:
            if distance[edge] == -1:
                queue.append(edge)
                distance[edge] = distance[node_index] + 1
    return distance[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
