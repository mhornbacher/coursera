# python3

import sys, threading
import time
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrderWalk(self, index):
    if self.left[index] > 0:
      self.inOrderWalk(self.left[index])
    self.result.append(self.key[index])
    if self.right[index] > 0:
      self.inOrderWalk(self.right[index])

  def inOrder(self, index=0):
    self.result = []
    if self.left[index] > 0:
      self.inOrderWalk(self.left[index])
    self.result.append(self.key[index])
    if self.right[index] > 0:
      self.inOrderWalk(self.right[index])

    return self.result

  def preOrderWalk(self, index):
    self.result.append(self.key[index])
    if self.left[index] > 0:
      self.preOrderWalk(self.left[index])
    if self.right[index] > 0:
      self.preOrderWalk(self.right[index])

  def preOrder(self, index=0):
    self.result = []
    self.result.append(self.key[index])
    if self.left[index] > 0:
      self.preOrderWalk(self.left[index])
    if self.right[index] > 0:
      self.preOrderWalk(self.right[index])

    return self.result

  def postOrderWalk(self, index):
    if self.left[index] > 0:
      self.postOrderWalk(self.left[index])
    if self.right[index] > 0:
      self.postOrderWalk(self.right[index])
    self.result.append(self.key[index])

  def postOrder(self, index=0):
    self.result = []
    if self.left[index] > 0:
      self.postOrderWalk(self.left[index])
    if self.right[index] > 0:
      self.postOrderWalk(self.right[index])
    self.result.append(self.key[index])

    return self.result

def main():
  tree = TreeOrders()
  tree.read()
  print(" ".join(str(x) for x in tree.inOrder()))
  print(" ".join(str(x) for x in tree.preOrder()))
  print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
