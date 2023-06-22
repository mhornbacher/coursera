#Uses python3
import sys
import math

# def build_graph_1(x, y):
#     graph = []
#     for i in range(len(x)):
#         graph.append([])
#         for k in range(len(x)):
#             tmp = math.sqrt(((x[i] - x[k]) ** 2) + ((y[i] - y[k]) **2))
#             graph[i].append(tmp)
#     return graph

def build_edges(x, y):
    edges = []
    for i in range(len(x)):
        for k in range(len(x)):
            dist = math.sqrt(((x[i] - x[k]) ** 2) + ((y[i] - y[k]) **2))
            edges.append([i, k, dist])
    return edges


class PriorityQueue:
    def __init__(self, size):
        self.parent = [x for x in range(size)]
        self.rank = [0] * size

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        elif self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1

def Kruskal(x, y):
    edges = build_edges(x, y)
    queue = PriorityQueue(len(x))
    result = 0.
    # sort the edges
    edges.sort(key=lambda x: x[-1])
    edges = edges[len(x):] #Remove all the 0 lengths (self to self)
    for edge in edges:
        if queue.find(edge[0]) != queue.find(edge[1]):
            result += edge[2] # append the join to a res array to get all the edges
            queue.union(edge[0], edge[1])
    return result

def minimum_distance(x, y):
    result = 0.
    # graph = build_graph_1(x, y)
    result = Kruskal(x, y)
    #write your code here
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
