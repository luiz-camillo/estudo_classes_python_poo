def potencia (base, expoente=2):
    return pow(base, expoente)


base = int(input('Digite o valor da base: '))
expoente = input('Digite o valor do expoente: ')

if expoente:
    print(f'O resultado é: {potencia(base, int(expoente))}')
else:
    print(f'O resultado é: {potencia(base)}')
