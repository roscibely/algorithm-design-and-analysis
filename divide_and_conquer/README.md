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