#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
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
                new_index = max(tree) + 1 # get the next open index
                currentNode[currentSymbol] = new_index # point this letter to that index
                currentNode = tree[new_index] = {} # point this tree to that index
    # my code ends
    return tree # return the tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
