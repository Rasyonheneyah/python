notas = []
namedia = []
notaver = []
def verifnotas():
    while True:
        nota = float(input("Insira uma nota: "))
        if nota == -1:
            break
        notas.append(nota)
    print(f'{len(notas)} notas foram lidas')
    print("Notas: ", ' '.join(map(str, notas)))
    qntd = len(notas)
    soma = 0
    for i in range(qntd):
        print(notas[qntd -1 -i])
        soma += notas[i]
    media = soma/len(notas)
    print(f'A soma é {soma}, e a média é igual a {media}')
    c = 0
    c2 = 0
    for i in notas:
        if i > media:
            c = c + 1     
        if c2 < 7:
            c2 = c2 +1
    print(f'{c} nota(s) acima da média e {c2} nota(s) abaixo de 7.')
    print("Você finalizou a verificação das notas!!!")
verifnotas()