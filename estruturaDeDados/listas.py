lista = ['Maçã', 'Banana', 'Uva']
print(lista)
lista[0] = 10
lista.append(True)
lista.insert(5, 'Banana 2 ')
print(lista[0])
print(lista)

texto = ['comidas.append(lista) Não faz a transferencia correta, transfere como um elemento da lista, tipo o [1]']
lista.extend(lista)

lista.insert(2, [9])
lista[2:4] = texto[0]
print(lista)
