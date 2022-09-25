# problema do da capacidade do pendrive com algoritmo guloso

def greedy(capacidade, lista):
    """Algoritmo guloso para o problema do pendrive
    
    Args:
        capacidade (int): capacidade do pendrive
        lista (list): lista de arquivos
    Returns:
        list: lista de arquivos que cabem no pendrive
    
    """
    lista.sort(reverse=True)
    soma = 0
    for i in lista:
        soma += i
        print('Arquivo: ',i, 'Mb')
        print('Espaço total ocupado', soma, 'Mb')
        if soma >= capacidade:
            print('Capacidade total do pendrive atingida')
            return lista.index(i) + 1
    return 0

if __name__ == '__main__':
    capacidade = 90
    lista = [10,15,20,20,30,35, 40,50]
    greedy(capacidade, lista)