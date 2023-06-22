# python3
import sys

NA = -1

class Node:
    def __init__ (self):
        self.next = [NA] * 4


def build_trie(patterns):
    new_index = 1
    tree = dict()
    tree[0] = {}
    # write your code here
    for pattern in patterns: # for each pattern
        currentNode = tree[0] # this is the first item in the tree
        for i in range(len(pattern)): # for each letter in the pattern
            currentSymbol = pattern[i] # get that letter in that pattern
            if currentSymbol in currentNode: # if we have that letter at this point in the tree
                currentNode = tree[currentNode[currentSymbol]] # keep walking down that path
            else: # we do not have this pattern in the tree
                new_index # get the next open index
                currentNode[currentSymbol] = new_index # point this letter to that index
                currentNode = tree[new_index] = {} # point this tree to that index
                new_index += 1
    # my code ends
    return tree # return the tree

def prefixTrieMatching(Text, Trie):
    position = 0
    symbol = Text[position]
    v = Trie[0]
    while True:
        if symbol in v:
            position += 1
            v = Trie[v[symbol]]
            # if we reach an endpoint
            if v == {}:
                return True
            try:
                symbol = Text[position]
            except IndexError:
                return False
        else:
            return False

def TrieMatching(Text, Trie):
    result = []
    for i in range(len(Text)):
        text = Text[i:]
        if prefixTrieMatching(text, Trie):
            result.append(i)
    return result


def solve (text, n, patterns):
    result = []

    # write your code here
    trie = build_trie(patterns)
    return TrieMatching(text, trie)

text = sys.stdin.readline().strip()
n = int (sys.stdin.readline().strip())
patterns = []
for i in range (n):
    patterns += [sys.stdin.readline().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
