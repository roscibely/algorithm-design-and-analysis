# Backtracking 

### Tentativa e erro

Um algoritmo de tentativa e erro é um algoritmo de resolução de problemas que usa uma abordagem de força bruta para encontrar a saída desejada. A abordagem da força bruta tenta todas as soluções possíveis e escolhe as soluções desejadas/melhores.


Na tentativa e erro, se a solução atual não for adequada, retrocedemos e tentamos encontrar outras soluções. Por isso, a recursão é usada. Essa abordagem é usada para resolver problemas que têm várias soluções.

* Existem três tipos de problemas no backtracking:

     1. Problema de Decisão - Busca por uma solução viável
     2. Problema de Otimização – Procure a melhor solução
     3. Problema de Enumeração - Encontre todas as soluções viáveis

### Exemplos: 

    Problema 1) Implemente um algoritmo que recebe como entrada um vetor de letras e encontre toda a ordem possível de arranjos de um determinado conjunto de letras. Quando escolhemos um par, aplicamos o backtracking para verificar se esse par exato já foi criado ou não. Se ainda não tiver sido criado, o par será adicionado à lista de respostas, caso contrário, será ignorado.
            Exemplo: Dado como entrada ['a', 'b', 'c']. A saída deve ser ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']. 
