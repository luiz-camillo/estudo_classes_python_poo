

estoque = ['up', 'gol', 'voyage', 'touareg', 'golf', 'passat']


checagem = input('Digite o nome do veículo que você deseja comprar: ').strip().lower()


if checagem in estoque:
    print(f'O veículo {checagem.upper()} está disponível em estoque!')
else:
    print(f'O veículo {checagem.upper()} não está disponível em estoque!')