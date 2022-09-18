def fibonacciBottomUp(n, table = {}):
    table[0] = 0
    table[1] = 1
    for cont in range(2, n + 1):
        table[cont] = table[cont - 1] +  table[cont - 2]
    return table[n]