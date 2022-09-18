def fibonacciTopDown(n, table = {}):
    if n == 1 or n == 0:
        return n
    try:
        return table[n]
    except:
        table[n] = fibonacciTopDown(n-1) + fibonacciTopDown(n-2)
        return table[n]


if __name__ == "__main__":
    print(fibonacciTopDown(10))
    