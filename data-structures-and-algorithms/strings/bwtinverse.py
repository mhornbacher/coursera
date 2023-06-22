# python3
import sys

class Counter:
    def __init__(self, string_array):
        self.last_row = [] # the number of letter x in the last row
        self.counters = [0] * 5 # the total numbers of $ A C G and T in the array
        for char in string_array:
            index = self.char_to_counter_index(char)
            self.counters[index] += 1
            self.last_row.append(self.counters[index])

    def char_to_counter_index(self, char):
        res = {"$": 0, "A": 1, "C": 2, "G": 3, "T": 4}
        return res[char]

    def last_to_first(self, char, index):
        char_index = self.last_row[index]
        counter_index = self.char_to_counter_index(char)
        result = sum(self.counters[0:counter_index]) + char_index
        return result

def InverseBWT(bwt):
    # write your code here
    last_row = list(bwt)
    first_row = sorted(last_row)
    counter = Counter(last_row)

    final_chars = [] # array to store all the chars for the final string
    index = 0
    for i in range(len(first_row)):
        first_row_char = first_row[index]
        # print("Getting first row\t", first_row_char, index, first_row)
        final_chars.append(first_row_char)
        index = counter.last_to_first(last_row[index], index) - 1 # 0 based indexing so you have to subtract one from the function

    return "".join(final_chars[::-1])


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))