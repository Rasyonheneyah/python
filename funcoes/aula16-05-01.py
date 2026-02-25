#
precototal=0
cdesconto=0.90
lista=["Arroz","Ovos","Café","Refrigerante","Pão"]
arroz= 50.00
cafe= 40.00
ovos= 30.00
refrigerante= 15.00
pao= 8.50
listacompras=[]
qtd=0

#3
def lista():
    lista=["Arroz          ","Cartela de Ovos","Café           ","Refrigerante   ","Pão de forma   "]
    arroz= 50.00
    cafe= 40.00
    ovos= 30.00
    refrigerante= 15.00
    pao= 8.50
    listapreco=[arroz, cafe, ovos, refrigerante, pao]
    n= len(lista)
    print("Num |      Produto     |   Preço em R$   ")
    for i in range (n):
        print(i+1,"  | ", lista[i], "   |     " ,listapreco[i])
#1    
def calc():
    preco=float(input("Insira o preço do produto: "))
    quantidade=float(input("Insira a quantidade de produto que foi comprada: "))
    precototal= preco*quantidade
    print(f'Total da compra: {precototal}')
#2
def desconto():
    total=float(input("Insira o total da compra: "))
    if total>100:
        totalcdesconto= total*cdesconto
        print(f'Total da compra com desconto: {totalcdesconto}')
#4
def comprar():
    print("Digite Fim para finalizar a lista de produtos")
    flag= True
    while flag:
        compras=input("Insira o item: ")
        if compras== "Fim":
            flag=False
        else:
            
            listacompras.append(compras)
    print(*listacompras, sep="; ")        

#5
def verif():
    lista=["Arroz","Ovos","Café","Refrigerante","Pão"]
    c=0
    print("Veficação de estoque.")
    produto=input("Insira o nome para a verificação: ")
    qtd= len(lista)
    for i in range(5):
        if lista[i] in produto:
            print("O produto está disponível!")

        else:
            c=c+1
    if c==5:
        print("O Produto não está disponível.")

#6
def contagem():
    flag= True
    while flag:
        compras=input("Insira o item: ")
        if compras== "Fim":
            flag=False
        else:
            n= len(compras)
            
            if compras[i] in compras:
                 for compras[i] in range(n):
                     if compras[i]==0:
                         pass
                     
            else:
                listacompras.append(compras)
    print(*listacompras, sep="; ")    
verif()
