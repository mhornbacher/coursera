# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    finished = False
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i))
            pass

        if next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack) > 0: #.pop throws an error if it is empty
                last_bracket = opening_brackets_stack.pop()
                if not last_bracket.Match(next):
                    print(i + 1)
                    finished = True
                    break
            else: # If it is empty we do not have a beginning for it
                print(i + 1)
                finished = True
                break
            pass

    # Printing answer, write your code here
    if not finished:
        if len(opening_brackets_stack) > 0:
            print(opening_brackets_stack.pop().position + 1)
        else:
            print("Success")
