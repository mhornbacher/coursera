# Uses python3
def edit_distance(string1, string2):
    distances = [[0] * (len(string2) + 1) for char in range(len(string1) + 1)] # Create the grid full of 0's
    distances[0] = [char for char in range(len(string2) + 1)] # fill the first row
    for i in range(len(string1) + 1):
        distances[i][0] = i # Fill the top row
    # show_distance(distances) # Show us the results
    # Fill arrays horizontally
    for i in range(1, len(string1) + 1): # for every letter in the first string
        for j in range(1, len(string2) + 1): # for every letter in the second letter
            # For some reason (magic) these numbers are the edit distance
            insertion = distances[i][j-1] + 1
            deleation = distances[i-1][j] + 1
            match = distances[i - 1][j - 1]
            mismatch = distances[i - 1][j-1] + 1
            # if it is the same use match otherwise use mismatch. Get the min to find the lowest edit distance
            if string1[i - 1] == string2[j - 1]:
                distances[i][j] = min(insertion, deleation, match)
            else:
                distances[i][j] = min(insertion, deleation, mismatch)
    # show_distance(distances) # Show Table for Debugging
    return distances[-1][-1] # Return Edit Distance

# Debugging: print the table
def show_distance(distances):
    for distance in distances:
        print(distance)

if __name__ == "__main__":
    print(edit_distance(input(), input()))
