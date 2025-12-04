



countries = {'brasil': 'brasilia',
            'argentina': 'buenos aires',
            'estados unidos': 'washington',
            'chile': 'santiago',
            'australia': 'canberra'
             }

pais = input('Digite o nome do pais que deseja saber a capital: ').lower().strip()


if pais in countries:
    print(f'A capital de {pais} é {countries[pais]}')
else:
    print('O país digitado não está listado')