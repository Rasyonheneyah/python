# Função recursiva de um número binário.

n=int(input("Digite um número: "))
a=0
b=-1
lista=[]
resposta=0
contador=0
while n!=1:
    while n != 1:
        a=n%2
        n=n//2
        lista.append(a)
        b=b+1
    lista.append(1)
    lista.reverse()
print(*lista, sep="")
# asterisco -> sem colchetes
# sep="" -> sem espaço






























