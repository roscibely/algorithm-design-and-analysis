def knapsack(capacity, weights, values):
    """Return the maximum value of items that fit in the knapsack.
    Args:
        capacity (int): capacity of the knapsack
        weights (list): list of weights of items
        values (list): list of values of items
    Returns:
        int: maximum value of items that fit in the knapsack    
    """

    table = [[0 for x in range(capacity + 1)] for x in range(len(values) + 1)]


    for i in range(len(values) + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                table[i][w] = 0
            elif weights[i-1] <= w:
                table[i][w] = max(table[i-1][w], values[i-1] + table[i-1][w-weights[i-1]])
            else:
                table[i][w] = table[i-1][w]
    print(table)
    return table[len(values)][capacity]

if __name__ == "__main__":
    capacity = 8
    weights = [2, 3, 4, 5]
    values = [3, 5, 6, 10]
    print(knapsack(capacity, weights, values))
