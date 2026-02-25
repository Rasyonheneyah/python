'''
Lista=[8,9,5]
#Leitura através dos indices
for i in range(3):
    print(i, Lista[i])
#Leitura através dos elementos
for i in Lista:#[8,9,5]
    print(i)
# Inveter os índices ou elementos

n=3
for i in range(n):
    print(Lista[i], Lista[n-1-i])
print(i)
'''
'''
#Tabuada de qualquer numero de 10
flag=True
while flag:
    tabuada = int(input('Insira um valor: '))
    if tabuada<1 or tabuada>10:
        flag=False
    else:
        for i in range(10):
            print(i+1,'x', tabuada,'=',  tabuada*(i+1))


'''
'''
base=int(input('Insira a Base: '))
e=int(input('Insira o expoente: '))
resultado= base**e
print(resultado)
'''
'''
#Inserir números numa lista
lista=[]
flag=True
while flag:
    numero= int(input('Insira um número: '))
    if numero == -1:
        flag=False
    else:
        lista.append(numero)
print('O valor total desses números e de: ', lista)
'''
'''
pares=0
impares=0
for i in range(10):
    numero=int(input('Insira um número: '))
    if numero %2==0:
      pares = pares+1
    else:
        impares=impares+1
print('Impares: ', impares)
print('Pares: ', pares)
'''
lista=[]
