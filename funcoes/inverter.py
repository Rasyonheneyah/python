# aula 11 ex 04

def inverter(x):
    i= ''.join(reversed(x))
    print(i)


n=input("Insira um número: ")
inverter(n)

# informar qntd de digitos

def informar(x):
    x = str(x)
    x = len(x)
    return x

n=int(input("Digite um número: "))
digitos =informar(n)
print(digitos)


