# python3
import math

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps_naive(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]
  # MY CODE STARTS HERE
  # -------------Min-Heap-----------------------
  # Auto generate the index of the elements in the heap
  def Parent(self, i):
    return math.ceil(i/2) - 1
  def LeftChild(self, i):
    return (2 * i) + 1
  def RightChild(self, i):
    return (2 * i) + 2
  # Move the item up untill it is larger then the item on top of it
  def SiftUp(self, i):
    while i > 0 and self._data[self.Parent(i)] > self._data(i): # While i is not root (the 0 index) and its parent
      self._data[self.Parent(i)], self._data[i] = self._data[i], self._data[self.Parent(i)]
      i = self.Parent(i)
  # Move the item untill both its children are less then it
  def SiftDown(self, i):
    minIndex = i
    l = self.LeftChild(i)
    if l < len(self._data) and self._data[l] < self._data[minIndex]:
      minIndex = l
    r = self.RightChild(i)
    if r < len(self._data) and self._data[r] < self._data[minIndex]:
      minIndex = r
    if i != minIndex:
      self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
      self._swaps.append((i, minIndex))
      self.SiftDown(minIndex) # Call siftDown again until i==minIndex

  # Build the Min-Heap
  def BuildHeap(self):
    n = len(self._data)
    for i in range(math.ceil(n/2) + 1, -1, -1):
      self.SiftDown(i)

  def GenerateSwaps(self):
    self.BuildHeap()

  # def printTree(self, index):
  #   right = self.RightChild(index)
  #   left = self.LeftChild(index)
  #   right = 0 if right >= len(self._data) else self._data[right]
  #   left = 0 if right >= len(self._data) else self._data[left]
  #   return """   {}   \n /   \ \n{}  -  {}""".format(self._data[index], left, right)

  # MY CODE ENDS HERE

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
