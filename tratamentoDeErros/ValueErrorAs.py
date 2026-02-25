soma = 0
while soma !=10:
    print(f'Objetivo simples, você precisa fazer uma soma que resulte 10. Tente causar erros no aplicativo algumas vezes para testar o TRY EXCEPT CONTINUE: ')
    try:
        n1 = int(input('Insira número 1: '))
        n2 = int(input('Insira número 2: '))
        soma = n1 + n2
    except ValueError as name:
        print(f'Erro encontrado por causa do {name}')
        continue
    if soma > 10:
        print('Acima do esperado.')
    elif soma < 10:
        print('Abaixo do esperado.')
    elif soma ==10:
        print(f'Você conseguiu! A soma entre {n1} e {n2} resulta em {soma}! ')
