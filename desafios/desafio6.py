

while True:
    try:
        nr = float(input('Digite o número: '))
        break
    except ValueError:
        print('Digite apenas números! Verifique e tente novamente.')
        print('\n')


if nr >10:
    print('O número é maior que 10.')
else:
    print('O número é menor ou igual a 10.')
