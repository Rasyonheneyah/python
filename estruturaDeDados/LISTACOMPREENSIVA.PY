numeros = [ 8, 5, 4, 3]
n2 = []
for i in numeros:
    n2.append(i*2)


print(numeros)
print(n2)

print([i*2 for i in numeros])
print(["É par" if n2[0]//2 else "Impar"])

n2.clear()
