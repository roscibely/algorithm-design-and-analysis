# Divide and Conquer 

### Divisão e conquista 

Dividir e Conquistar é um paradigma algorítmico no qual o problema é resolvido usando a estratégia Dividir, Conquistar e Combinar.

Um algoritmo típico de Dividir e Conquistar resolve um problema usando as três etapas a seguir:

1. Dividir: Isso envolve dividir o problema em subproblemas menores.
2. Conquistar: Resolva subproblemas chamando recursivamente até ser resolvido.
3. Combine: Combine os subproblemas para obter a solução final de todo o problema.

Exemplo: 

```python
DivideAndConquer(a, m, n)
{
    if(subProblem(a, m, n))
      return(solution(a, m, n))
    else 
      p = divide(a, m, n)               
      b = DivideAndConquer(a, m, mid)                 
      c = DivideAndConquer(a, mid+1, n)            
      d = combine(b, c)                
   return(d)
}
```
#### Vantagens do Algoritmo Dividir e Conquistar

* O algoritmo de divisão e conquista é fácil e eficaz para resolver problemas difíceis, dividindo-os em subproblemas
* O algoritmo de divisão e conquista é frequentemente usado em algoritmos de classificação como classificação por mesclagem, classificação rápida, etc.
* Também é usado em algoritmos de busca como busca linear e busca binária
* É melhor usar o algoritmo de divisão e conquista ao lidar com números flutuantes.
     


#### Desvantagens do Algoritmo Dividir e Conquistar

* No algoritmo de divisão e conquista, a recursão do subproblema é lenta
* Para alguns problemas específicos, o método de dividir e conquistar torna-se complicado em comparação com o método iterativo