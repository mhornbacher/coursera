# python3
import sys

def BWT(text):
    n = len(text) # the length of the text, cached for operation below
    # for each letter in the text add the 0-ith chars to the end of the ith=last/nth chars
    bwt_array = sorted([text[i:n] + text[0:i] for i in range(n)]) # sort the resulting array as per the BWT spec
    # get the last letter from each of the items in the above array and return it
    return "".join([rotation[-1] for rotation in bwt_array]) # get the last char for each rotation in the array

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))