"""
Implementação do Bubble Sort com um verificador de ordenação.

O algoritmo percorre a lista comparando elementos adjacentes e realizando
trocas quando necessário, fazendo com que os menores valores "borbulhem"
para o início do vetor a cada iteração.

Durante cada passada também é feita uma verificação para identificar se
a sequência já se encontra ordenada. Caso nenhuma troca seja necessária,
o algoritmo pode encerrar antes de percorrer todo o vetor, evitando
iterações desnecessárias.
"""

def bubblesort(x):
    n = len(x)
    for i in range(0, n-1):
        j = n -1
        contador = j
        while j != i:    
            # Verifica se o elemento sucessor é menor que seu antecessor
            if x[j] < x[j-1]:
                # caso seja, ele inverte as posições
                x[j], x[j-1] = x[j-1], x[j]  
            
            # Verifica se o sucessor é maior que o antecessor, depois das posições   trocadas
            # para garantir que caso uma troque termine de ordenar os números, já saia do ciclo
            
            if x[j] > x[j-1]:
                contador-=1
            


            j-=1
        # Se o contador e o elemento borbulhado (j) chegou no último elemento (i) comparado, então a lista está ordenada corretamente.   
        if j == contador == i:
            print(f'Já está ordenada quando percorri no {i}º elemento')
            return x
            
    return x


vetor = [1,3, 4,6,2,5]
print(bubblesort(vetor))