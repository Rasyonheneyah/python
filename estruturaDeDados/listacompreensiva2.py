# Lista Compreensiva
frutas = ['pera','uva','maçã']
novalista = []
for x in frutas:
    novalista.append(x) if 'a' in x else None

print(novalista)


def maior(v):
    return v.upper()



print([maior(x) for x in frutas if 'u' in x])
print(x)
    
#f = frutas // FAZ AMBOS OCUPAREM MESMO ESPAÇO NA MEMÓRIA, SE VC MEXE EM F MEXE EM FRUTAS
f = frutas.copy()

f.append('Banana')
print(f)
print(frutas)
print(frutas.pop(1))
print(frutas)
