#calculadora imc

def calcular_imc(peso, altura):
    imc = peso // (altura**2)
    return imc
peso = float(input('Digite o seu peso em KG: '))
altura = float(input('Digite a sua altura: '))

imc = calcular_imc(peso, altura)

if imc < 18.5:
    print(f'IMC: {imc:.2f} - Abaixo do peso')
elif imc < 25:
    print(f'IMC: {imc:.2f} - Peso normal')
elif imc < 30:
    print(f'IMC: {imc:.2f} - Sobrepeso')
elif imc < 35:
    print(f'IMC: {imc:.2f} - Obesidade grau I')
elif imc < 40:
    print(f'IMC: {imc:.2f} - Obesidade grau II')
else:
    print(f'IMC: {imc:.2f} - Obesidade grau III (mórbida)')