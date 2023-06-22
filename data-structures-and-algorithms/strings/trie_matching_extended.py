# python3
import sys

NA = -1
NEXT_CHARS = {'A': 0, 'C': 1, 'G': 2, 'T': 3 }

class Node:
    def __init__ (self):
        self.next = [NA] * 4
        self.patternEnd = False


def build_trie(patterns):
    new_index = 1
    tree = dict()
    tree[0] = {}
    # write your code here
    for pattern in patterns: # for each pattern
        last_pattern_index = len(pattern) - 1
        currentNode = tree[0] # this is the first item in the tree
        for i in range(len(pattern)): # for each letter in the pattern
            currentSymbol = pattern[i] # get that letter in that pattern
            if currentSymbol in currentNode: # if we have that letter at this point in the tree
                if i == last_pattern_index:
                    currentNode[currentSymbol][1] = True
                currentNode = tree[currentNode[currentSymbol][0]] # keep walking down that path
            else: # we do not have this pattern in the tree
                if i == last_pattern_index:
                    currentNode[currentSymbol] = [new_index, True]
                else:
                    currentNode[currentSymbol] = [new_index, False] # point this letter to that index
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
            if v[symbol][1] == True:
                return True
            position += 1
            v = Trie[v[symbol][0]]
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

    # return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
    patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
