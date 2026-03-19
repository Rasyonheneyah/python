"""
Implementação do algoritmo Selection Sort, que realiza a ordenação de uma
lista selecionando iterativamente o menor elemento da parte não ordenada
e posicionando-o em seu local correto.

Como melhoria geral de desempenho, pode-se prever um mecanismo para
interromper o processo caso seja detectado que a lista já se encontra
ordenada, evitando iterações desnecessárias.
"""
def selectionSort(x):

    n = len(x)
    for i in range(0, n-1):
        
        # Sistema de verificação no SelectionSort        
        flag = False
        j = i+1

        for k in x[j:]:
            if k < x[i]:
                flag = True
        # Se a verificação achou um elemento no resto da lista menor que
        # o elemento atual, ele dá prosseguimento com a ordenação
        # se não, é finalizado e retorna
        if flag:
            
            while j != n:
                if x[i] > x[j]:
                    x[i], x[j] = x[j], x[i]
                j+= 1

        
    return x



vetor = [1, 3, 4, 5, 2]
print(selectionSort(vetor))
