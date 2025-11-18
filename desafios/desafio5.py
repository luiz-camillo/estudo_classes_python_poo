
#usando metodo count

frutas = ['Maçã', 'Uva', 'Maçã', 'Melão', 'Maçã', 'Abacate', 'Maracujá']

qtd = frutas.count('Maçã')

print(f'A fruta Maçã, possui {qtd} registros na lista de frutas ')


#usando for loop

counter = 0

for fruta in frutas:
    if fruta == 'Maçã':
        counter += 1
print(f'A fruta Maçã, possui {counter} registros na lista de frutas')