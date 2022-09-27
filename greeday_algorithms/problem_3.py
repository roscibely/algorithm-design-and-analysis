# problema da mochila fracionada com objetos fracionados com algoritmo guloso

def greedy(capacidade_da_mochila, pesos, valores):
    """Algoritmo guloso para o problema da mochila fracionada
    Args:
        capacidade_da_mochila (int): capacidade da mochila
        pesos (list): lista de pesos
        valores (list): lista de valores
    Returns:
        list: lista de pesos que cabem na mochila
    """
    soma = 0
    for i in range(len(pesos)):
        if capacidade_da_mochila - pesos[i] < 0:
            termo_div = pesos[i]/capacidade_da_mochila
            capacidade_da_mochila -= int(pesos[i]/termo_div)
            soma += valores[i]
            print('Peso: ', pesos[i]/termo_div, 'Kg')
            print('Valor total: ', soma, 'R$')
        else:
            capacidade_da_mochila -= pesos[i]
            soma += valores[i]
            print('Peso: ', pesos[i], 'Kg')
            print('Valor total: ', soma, 'R$')
        if capacidade_da_mochila <= 0:
            print('Capacidade total da mochila atingida')
            return i + 1
    return 0

if __name__ == '__main__':
    capacidade_da_mochila = 50
    pesos = [10, 20, 30]
    valores = [60, 100, 120]
    greedy(capacidade_da_mochila, pesos, valores)

