def mochila(capacidade, pesos, valores, n):
    """
    Args: 
        capacidade (int): capacidade da mochila
        pesos (list): lista de pesos dos itens
        valores (list): lista de valores dos itens
        n (int): número de itens
    Returns: 
        int: valor máximo que a mochila pode carregar     
    """

    if n == 0 or capacidade == 0:
        return 0

    if pesos[n-1] > capacidade: 
        return mochila(capacidade, pesos, valores, n-1)

    else:
        return max(valores[n-1] + mochila(capacidade-pesos[n-1], pesos, valores, n-1), mochila(capacidade, pesos, valores, n-1))

if __name__ == "__main__":
    capacidade = 8
    pesos = [2, 3, 4, 5]
    valores = [3, 5, 6, 10]
    print(mochila(capacidade, pesos, valores, len(valores)))