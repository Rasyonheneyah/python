#Função Recursiva de uma PA
an=int(input("Digite um número para ser o a1:  "))
r=int(input("Digite um número para ser a razão: "))
n=int(input("Digite o enésimo número: "))
contador=1
print("a 1    ->", an) 
c=True
e=1
while c==True:
    e=e+1
    an= an+r
    print("a",e,"   ->", an)
    contador=contador+1
    if contador==n:
        c=False
