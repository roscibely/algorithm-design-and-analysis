# problema da mochila com programação dinâmica com recursão e memoização

def mochila(capacidade, pesos, valores, n, memo):
    """
    Args: 
        capacidade (int): capacidade da mochila
        pesos (list): lista de pesos dos itens
        valores (list): lista de valores dos itens
        n (int): número de itens
        memo (dict): dicionário para memoização
    Returns: 
        int: valor máximo que a mochila pode carregar     
    """

    if n == 0 or capacidade == 0:
        return 0

    if (capacidade, n) in memo:
        return memo[(capacidade, n)]

    if pesos[n-1] > capacidade: 
        memo[(capacidade, n)] = mochila(capacidade, pesos, valores, n-1, memo)
        return memo[(capacidade, n)]

    else:
        memo[(capacidade, n)] = max(valores[n-1] + mochila(capacidade-pesos[n-1], pesos, valores, n-1, memo), mochila(capacidade, pesos, valores, n-1, memo))
        return memo[(capacidade, n)]

if __name__ == "__main__":
    capacidade = 8
    pesos = [2, 3, 4, 5]
    valores = [3, 5, 6, 10]
    memo = {}
    print(mochila(capacidade, pesos, valores, len(valores), memo))
    print(memo)