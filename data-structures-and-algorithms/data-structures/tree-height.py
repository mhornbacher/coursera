# python3

import sys, threading
from queue import Queue
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.height = 0
    def addChild(self, node):
        self.children.append(node)
    def setHeight(self, height):
        self.height = height

    def __str__(self):
        return "Node: value -> " + str(self.value) + "; height -> " + str(self.height)

    def __repr__(self):
        return "Node: value -> " + str(self.value) + "; height -> " + str(self.height)

class TreeHeight:
    def __init__(self, n=0, parent=[]):
        self.n = n
        self.parent = parent
        self.setup()

    def read(self):
            self.n = int(sys.stdin.readline()) # The first line is n
            self.parent = list(map(int, sys.stdin.readline().split())) # The second line of inputs
            self.setup()

    def setup(self):
            #Create the Array of nodes
            self.nodes = [Node(i) for i in range(self.n)]
            
            # Debug
            # print("-------Nodes---------")
            # for node in self.nodes:
            #     print(node)

            for child_index in range(len(self.nodes)):
                parent_index = self.parent[child_index] # get the parent index that was passed in
                if parent_index == -1: # If it is the root
                    self.root = self.nodes[child_index] # set that node as the root
                    self.root.setHeight(1) # set the initial height
                else:
                    self.nodes[parent_index].addChild(self.nodes[child_index])

            # Debug
            # print("--------Nodes With Children--------")
            # for node in self.nodes:
            #     print(node, node.children)

    def compute_height_slow(self):
            # Replace this code with a faster implementation
            maxHeight = 0
            for vertex in range(self.n):
                    height = 0
                    i = vertex
                    while i != -1:
                            height += 1
                            i = self.parent[i]
                    maxHeight = max(maxHeight, height);
            return maxHeight;

    def compute_height(self):
        #Write code to return computed height
        if not self.root: #If there is no root return 0
            return 0

        queue = Queue()
        queue.put(self.root)
        max_height = 0

        while not queue.empty():
            current = queue.get_nowait()
            if current.height > max_height:
                max_height = current.height
            # print("-------IN QUEUE-------")
            # print(current)
            for child in current.children:
                child.setHeight(current.height + 1)
                queue.put(child)
        return max_height

def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())
    # print(tree.compute_height_slow())


def test(): #TODO have it generate trees
    tree = TreeHeight(5, [4, -1, 4, 1, 1])
    slow = tree.compute_height_slow()
    faster = tree.compute_height()
    print(slow, ":", faster)
    if slow != faster:
        print("Error!")

threading.Thread(target=main).start()
# threading.Thread(target=test).start()
