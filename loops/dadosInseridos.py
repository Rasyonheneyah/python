f= 'feminino'
m= 'masculino'
s= 'solteiro'
c= 'casado'
v= 'viuvo'
d= 'divorciado'
nome=input('Insira o seu nome: ')
while len(nome)<4:
    nome=input('Insira um nome com mais de 3 caracteres: ')
idade=int(input('Insira sua idade: '))
while idade<0 or idade>150:
    idade=int(input('Insira uma idade entre 0 e 150: '))
salario= int(input('Insira o valor do seu salario: '))
while salario<0:
    salario=int(input('Insira um salario positivo: '))
sexo=input('Qual o seu sexo? feminino / masculino ')
while sexo!=f and sexo!=m:
    sexo=input('feminino / masculino ')
estado_civil=input('Qual o seu estado civil? solteiro / casado / viuvo / divorciado: ')
while estado_civil!= s and estado_civil!=c and estado_civil!=v and estado_civil!=d:
    estado_civil=input('solteiro / casado / viuvo / divorciado ')

print('Obrigado por fornecer todos esses dados meu companheiro!')
print('Nome: ', nome)
print('Idade: ', idade)
print('Salario: ', salario)
print('Sexo: ', sexo)
print('Estado Civil: ', estado_civil)