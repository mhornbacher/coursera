# Uses python3
import sys

def optimal_weight(total_Weight, weights):
    if len(weights) == 0 or min(weights) > total_Weight: # If the smallest item does not fit or there are no items
        return 0 # Return that there is no total weight of gold that we can take
    else: # Get the maximum combination for the space we have
        max_weights = [[0] * (total_Weight + 1) for x in range(len(weights))] # Create an array of the number of weights by the weight of the bag + 1 full of 0's
        max_weights[0] = [weights[0] if weights[0] <= j else 0 for j in range(total_Weight + 1)] # fill in the first row with items assuming we can only take the first item
        for i in range(1, len(weights)): #For every item apart from the first one
            for j in range(1, total_Weight + 1): # For every item in the knapsack
                weight = max_weights[i - 1][j] # Get the same weight of the previous row
                if weights[i] <= j: # if we can add the current weight
                    max_weight = (max_weights[i - 1][j - weights[i]]) + weights[i] # get the max weight if we add this row
                    if weight < max_weight: # if it is more them the last row (a.k.a without it)
                        weight = max_weight # it is the new weight
                        max_weights[i][j] = weight # Save it
                    else:
                        max_weights[i][j] = weight # adding this is pointless
                else:
                    max_weights[i][j] = weight # we cannot add the current weight

        return max_weights[-1][-1] # return the result


if __name__ == '__main__':
    input = sys.stdin.read() # get multiple lines
    W, n, *w = list(map(int, input.split())) # split the input accordingly
    print(optimal_weight(W, w)) # print the result
