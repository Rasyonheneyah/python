# 4. Nome na vertical em escada. Modifique o programa anterior
# de forma a mostrar o nome em formato de escada.

def repeatName():
    nomel = ""
    nome = input('Digite o seu nome: ')
    vezes = int(input("Digite a quantidade de vezes: " ))
    while vezes-1!=0:
        for i in nome:
            nomel = nomel + i
            print(nomel)
        tamn = len(nome)
        for i in range(len(nome)):
            print(nomel)
            nomel = nomel[:-1]

repeatName()
