paisa= int(input('Insira população do Pais A: '))
cresca= float(input('Insira taxa de crescimento em decimal do país A (ex 0.5 para 50%): '))
cresca=cresca+1
crescb=float(input('Insira taxa de crescimento em decimal do país B (ex 0.5 para 50%): '))
crescb=crescb+1
paisb= int(input('Insira o valor de habitantes do país B'))
contagem=0
paisa=float(paisa)
paisb=float(paisb)
while paisa<paisb:
    paisa= paisa*cresca
    paisb=paisb*crescb
    contagem= contagem +1
print('Levou ', contagem, 'anos para que o país A fique com A fique com mais habitantes que o B')
print('Pais A-> ', paisa)
print('País B-> ',paisb )