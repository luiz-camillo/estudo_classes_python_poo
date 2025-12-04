def dobro(x):
    return x *2

def quadrado(y):
    return dobro(y) ** 2

numero = int(input('Digite um número inteiro: '))

print(f'O quadrado do dobro de {numero} é {quadrado(numero)}')