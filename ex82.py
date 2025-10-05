lista1 = list()
pares = list()
impares = list()
while True:
    lista1.append(int(input('Digite Uma valor: ')))
    resp = str(input('Quer Continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(lista1):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {lista1}')
print(f'Os numeros pares na lista são {pares}')
print(f'Os numeros pares na lista são {impares}')
