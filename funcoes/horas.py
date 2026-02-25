# Funções Converter e Saida para hora AM / PM



def converter(hora, minuto):
    if hora>12:
        hora= hora - 12
    return(hora, minuto)

def saida(hora, resultado):
    if hora>12:
        print(f'{resultado[0]}:{resultado[1]} P')
    else:
        print(f'{resultado[0]}:{resultado[1]} A')

flag= True
while flag: 
    hora=int(input("Digite a hora: "))
    if hora<0:
        flag= False
    else:
        minuto= int(input("Digite o minuto: "))

        if hora>=0 and hora<=24 :
            resultado= converter(hora, minuto)
            saida(hora, resultado)
        else:
             print("Hora inválida!")

# print (f'{hora}:{minuto}')
#print(resultado)
