import time

class FibonacciSequence():

    def __init__(self):
        """
        The constructor for the FibonacciSequence class.
        """
        pass


    def fibonacciRecursive(self, n,):
        """
        A recursive approach to the Fibonacci Sequence.

        Args:
            n (int): The number of the Fibonacci Sequence to return.
        Returns:
            int: The value of the Fibonacci Sequence at the nth position.
        """
        if n == 1 or n == 0:
            return n
        return self.fibonacciRecursive(n-1) + self.fibonacciRecursive(n-2)


    def fibonacciBottomUp(self, n, table = {}):
        """
        A bottom-up approach to the Fibonacci Sequence.

        Args: 
            n (int): The number of the Fibonacci Sequence to return.
            table (dict): A dictionary to store the Fibonacci Sequence values.
        Returns:
            int: The value of the Fibonacci Sequence at the nth position.
        """
        table[0] = 0
        table[1] = 1
        for cont in range(2, n + 1):
            table[cont] = table[cont - 1] +  table[cont - 2]
        return table[n]
    

    def fibonacciTopDown(self, n, table = {}):
        """
        A top-down approach to the Fibonacci Sequence.

        Args:
            n (int): The number of the Fibonacci Sequence to return.
            table (dict): A dictionary to store the Fibonacci Sequence values.
        Returns:    
            int: The value of the Fibonacci Sequence at the nth position.
        """
        if n == 1 or n == 0:
            return n
        try:
            return table[n]
        except:
            table[n] = self.fibonacciTopDown(n-1) + self.fibonacciTopDown(n-2)
            return table[n]


if __name__ == "__main__":
    N= 40
    fibonacci = FibonacciSequence()
    start = time.time()
    print(fibonacci.fibonacciTopDown(N))
    end = time.time()
    print("Tempo Total de Execução - Fibonacci Top Down: ", round(end - start, 20)*(10**3), "milissegundos")

    start = time.time()
    print(fibonacci.fibonacciBottomUp(N))
    end = time.time()
    print("Tempo Total de Execução - Fibonacci Bottom Up: ", round(end - start, 20)*(10**3), "milissegundos")
    
    start = time.time()
    print(fibonacci.fibonacciRecursive(N))
    end = time.time()
    print("Tempo Total de Execução - Fibonacci Recursive: ", round(end - start, 20)*(10**3), "milissegundos")