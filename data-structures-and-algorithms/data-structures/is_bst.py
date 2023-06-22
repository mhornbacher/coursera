#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeOrders:
  def __init__(self, tree):
    self.tree = tree

  def inOrderWalk(self, index):
    node = self.tree[index]
    if node[1] > 0:
      self.inOrderWalk(node[1])
    self.result.append(node[0])
    if node[2] > 0:
      self.inOrderWalk(node[2])

  def inOrder(self, index=0):
    self.result = []
    node = self.tree[index]
    if node[1] > 0:
      self.inOrderWalk(node[1])
    self.result.append(node[0])
    if node[2] > 0:
      self.inOrderWalk(node[2])

    return self.result

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if len(tree) < 1:
    return True
  sorted_tree = TreeOrders(tree)
  sorted_tree = sorted_tree.inOrder()
  result = True
  i = 0
  while result and i < len(sorted_tree) - 1:
    i += 1 # move up an index
    if sorted_tree[i - 1] >= sorted_tree[i]: # check if the next element is smaller then the previous one
      result = False

  return result


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
