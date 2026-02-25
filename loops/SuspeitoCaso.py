"""
2. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um
crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação
sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2
questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5
como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

classif = {
    "Inocente": 1,
    "Suspeita": 2,
    "Cúmplice": 3 or 4,
    "Assassino": 5,
}
a = b = c = d = e = False
p1 = "Telefonou para a vítima?"
p2 = "Esteve no local do crime?"
p3 =  "Mora perto da vítima?"
p4 = "Devia para a vítima?"
p5 = "Já trabalhou com a vítima?"
perguntas=[p1, p2, p3, p4, p5]
contador = 0


for i in range(5):
    r = input(f'{perguntas[i]}')
    if r.lower == "sim":
        contador= contador + 1
if contador == 1:
    print("Você é inocente!")
elif contador == 2:
    print("Você é suspeito!")
elif contador > 2 and contador < 5:
    print("Você é o cúmplice!")     
else:
    print("Você é culpado!")