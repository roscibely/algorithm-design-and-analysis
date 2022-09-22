# Escrever uma função que recebe uma lista de moedas e um valor e retorna o número mínimo de moedas para fazer o troco do valor com recursão.


def troco(moedas, valor, memo = {}):
    """
    Args: 
        moedas (list): lista de moedas
        valor (int): valor a ser trocado
        memo (dict): dicionário para memoização
    Returns: 
        int: número mínimo de moedas para fazer o troco do valor
    """
    if valor == 0:
        return 0
    if valor < 0:
        return float('inf')
    if valor in memo:
        return memo[valor]
    memo[valor] = min([1 + troco(moedas, valor - moeda, memo) for moeda in moedas])

    return memo[valor]

if __name__ == "__main__":
    moedas = [5, 7]
    valor = 50
    print(troco(moedas, valor))
