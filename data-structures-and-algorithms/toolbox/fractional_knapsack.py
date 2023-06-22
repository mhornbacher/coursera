# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    unit_values = []
    for i in range(0, len(weights)):
        unit_values.append(values[i] / weights[i])
        
    while capacity > 0:
        if sum(unit_values) == 0:
            return value
        m = max(unit_values)
        index = [z for z, j in enumerate(unit_values) if j == m][0]
        unit_value = unit_values[index]
        unit_values[index] = 0
        if capacity > weights[index]:
            value += values[index]
            capacity -= weights[index]
        else:
            value += capacity * unit_value
            capacity -= capacity # So 0 right?
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
