#!/usr/bin/python3

import sys, threading
import random

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeOrders:
  def __init__(self, tree):
    self.tree = tree

  def inOrderWalk(self, index):
    node = self.tree[index]
    if node[1] > 0:
      self.inOrderWalk(node[1])
    self.result.append(node)
    if node[2] > 0:
      self.inOrderWalk(node[2])

  def inOrder(self, index=0):
    self.result = []
    node = self.tree[index]
    if node[1] > 0:
      self.inOrderWalk(node[1])
    self.result.append(node)
    if node[2] > 0:
      self.inOrderWalk(node[2])

    return self.result

  def isBinary(self):
    self.inOrder()
    for i in range(1, len(self.result)):
      if self.result[i - 1][0] > self.result[i][0]: # if the previous one is greater then the current one
        return False  # Then there it is not a binary tree at all
      elif self.result[i-1][0] == self.result[i][0]: # if they are equal (a.k.a there is a duplicate)
        # Check children of both for now
        if self.result[i][1] != -1:
          if self.tree[self.result[i][1]][0] == self.result[i][0]: # if the left child equals the parent
            return False # then it is not a valid tree
        if self.result[i][2] != -1:
          if self.tree[self.result[i-1][2]][0] < self.result[i][0]: # if the right child is less then the parent (I do not think this check is needed)
            return False # then it is not a valid tree
    return True

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if len(tree) < 1:
    return True
  sorted_tree = TreeOrders(tree)
  return sorted_tree.isBinary()

  # FIRST ATTEMPT
  # sorted_tree = sorted_tree.inOrder()
  # result = True
  # i = 0
  # while result and i < len(sorted_tree) - 1:
  #   i += 1 # move up an index
  #   if i < len(sorted_tree)-1 and sorted_tree[i - 1] > sorted_tree[i + 1]: # check if the next element is smaller then the previous one
  #     result = False
  #   elif sorted_tree[i - 1] >= sorted_tree[i]:
  #     return False

  # return result

# def IsBinarySearchTree(tree):
#   # Implement correct algorithm here
#   return True


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

# CUSTOM TESTING SUITE

def tree_to_c_input(tree_list):
  def rightChild(index):
    return 2 * index + 2
  def leftChild(index):
    return 2 * index + 1
  tmp = []
  res = []
  for i in range(len(tree_list)):
    if tree_list[i] is None:
      continue
    left = leftChild(i)
    right = rightChild(i)
    if left < len(tree_list) and tree_list[left]:
      left = tree_list[left]
    else:
      left = -1
    if right < len(tree_list) and tree_list[right]:
      right = tree_list[right]
    else:
      right = -1
    tmp.append(tree_list[i])
    res.append([tree_list[i], left, right])

  for row in range(len(res)):
    if res[row][1] > -1:
      res[row][1] = tmp.index(res[row][1]) 
    if res[row][2] > -1:
      res[row][2] = tmp.index(res[row][2])

  return res

def test():
  from binarytree import tree, bst, Node, inspect, pprint
  import time
  test_num = 0
  for i in range(0, 100):
    start_time = time.time()
    height = random.randint(10, 18)
    is_bst = bool(random.getrandbits(1))
    if is_bst:
      tmp_tree = bst(height=height)
    else:
      tmp_tree = tree(height=height)
    tmp_tree_input = tree_to_c_input(tmp_tree.to_list())
    starttime = time.time()
    my_code = IsBinarySearchTree(tmp_tree_input)
    answer = is_bst
    passed = my_code == is_bst
    print("Test #{}: {} ({}/{})\tHeight: {}\tNodes: {}\tTime: {}/{}".format(
      i, passed, my_code, answer, height, inspect(tmp_tree)['node_count'], time.time() - start_time, time.time() - starttime)
    )
    if not passed:
      print("FAILED")
      for line in tmp_tree_input:
        print(line)
      break

# threading.Thread(target=test).start()


def test2():
  print('Running examples...')
  example11 = ["1:1", True, [2, 1, 2], [1, -1, -1], [3, -1, -1]]
  example12 = ["1:2", False,[1, 1, 2], [2, -1, -1], [3, -1, -1]]
  example13 = ["1:3", True]
  example14 = ["1:4", True, [1, -1, 1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [5, -1, -1]]
  example15 = ["1:5", True, [4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [5, -1, -1], [7, -1, -1]]
  example16 = ["1:6", False,[4, 1, -1], [2, 2, 3], [1, -1, -1], [5, -1, -1]]
  # Hard Examples
  example21 = ["2:1", True, [2, 1, 2], [1, -1, -1], [3, -1, -1]]
  example22 = ["2:2", False, [1, 1, 2], [2, -1, -1], [3, -1, -1]]
  example23 = ["2:3", True, [2, 1, 2], [1, -1, -1], [2, -1, -1]]
  example24 = ["2:4", False, [2, 1, 2], [2, -1, -1], [3, -1, -1]]
  example25 = ["2:5", True]
  example26 = ["2:6", True, [2147483647, -1, -1]]
  example27 = ["2:7", True, [1, -1, 1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [5, -1, -1]]
  example28 = ["2:8", True, [4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [5, -1, -1], [7, -1, -1]]
  examples = [example11, example12, example13, example14, example15, example16, example21, example22, example23, example24, example25, example26, example27, example28]
  passed = True
  for example in examples:
    name = example[:1][0]
    result = IsBinarySearchTree(example[2:])
    answer = example[1:2][0]
    if result != answer:
      print("Failed {}: {} for {}/{}".format(name, result, answer, example[2:]))
      passed = False
  if passed:
    print("All Examples Passed")

# threading.Thread(target=test2).start()