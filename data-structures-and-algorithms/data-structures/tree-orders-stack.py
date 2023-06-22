# python3

import sys, threading
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

  def walk_down(self, i):
    while self.left[i] > 0:
      print(self.left[i])
      self.stack.append(i)
      i = self.left[i]

  def inOrder(self):
    self.result = []
    self.stack = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.walk_down(0)
    print(self.stack)
    while len(self.stack) > 0:
      node = self.stack.pop()
      self.result.append(node)
      if self.right[node]:
        self.walk_down(self.right[node])
    
    return self.result

  def preOrder(self, index=0):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
              
    return self.result

  def postOrder(self, index=0):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that

    return self.result

def main():
  tree = TreeOrders()
  tree.read()
  print(" ".join(str(x) for x in tree.inOrder()))
  print(" ".join(str(x) for x in tree.preOrder()))
  print(" ".join(str(x) for x in tree.postOrder()))
  # return tree

threading.Thread(target=main).start()
# tree = main()
