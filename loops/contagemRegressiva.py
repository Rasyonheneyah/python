def contagem_regressiva():
    numeros = int(input('Insira um número para a contagem regressiva!'))
    while numeros<=0:
        numeros=int(input('Insira um número inteiro positivo!'))
    while numeros>=0:
        print(numeros)
        numeros=numeros-1

contagem_regressiva()
