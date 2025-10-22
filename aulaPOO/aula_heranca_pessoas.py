class Pessoa:  # Classe pai
    def __init__(self, nome, idade):
        # Construtor: define atributos básicos da classe Pessoa
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        # Método que exibe uma apresentação da pessoa
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos de idade.')


class Funcionario(Pessoa):  # Classe filha que herda de Pessoa
    def __init__(self, nome, idade, cargo):
        # Chama o construtor da classe pai
        super().__init__(nome, idade)
        self.cargo = cargo  # Novo atributo específico

    def trabalhar(self):
        # Método específico da classe Funcionario
        print(f'{self.nome} está trabalhando como {self.cargo}.')


class Cliente(Pessoa):  # Classe filha que herda de Pessoa
    def __init__(self, nome, idade, saldo):
        # Chama o construtor da classe pai
        super().__init__(nome, idade)
        self.saldo = saldo  # Atributo adicional

    def comprar(self, valor):
        # Método que verifica se o cliente tem saldo suficiente
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Olá {self.nome}! Sua compra de R${valor:.2f} foi aprovada. Saldo atual: R${self.saldo:.2f}.')
        else:
            print(f'Olá {self.nome}! Saldo insuficiente.')

while True:
        nome = input('Digite o nome do funcionário: ')
        if nome.replace(" ", "").isalpha():
            break
        else:
            print(f'Formato inválido, {nome} não utilize números ou símbolos, apenas letras!')

while True:
        try:
            idade = int(input('Digite a idade do funcionário: '))
            break
        except ValueError:
                print(f'Fomato inválido,{nome} utilize apenas números')

while True:
        cargo = input(f'Digite o cargo do funcionário {nome}: ')
        if nome.replace(" ", "").isalpha():
            break
        else:
            print(f'Fomato inválido, {nome} não utilize números ou símbolos, apenas letras!')


print('\n')

f1 = Funcionario(nome, idade, cargo)
f1.apresentar()
f1.trabalhar()

print('\n')

while True:
    nome = input('Digite o nome do cliente: ')
    if nome.replace(" ", "").isalpha():
        break
    else:
        print(f'Formato inválido, {nome}  não utilize números ou símbolos, apenas letras!')

while True:
    try:
        idade = int(input('Digite a idade do funcionário: '))
        break
    except ValueError:
        print(f'Fomato inválido, {nome}  utilize apenas números')

while True:
    try:
        saldo = float(input('Digite o saldo do cliente: R$'))
        break
    except ValueError:
        print(f'Formato inválido, {nome} utilize apenas números reais')

c1 = Cliente(nome, idade, saldo)

print('\n')

while True:
    try:
        valor = float(input('Digite o valor da compra: R$'))
        break
    except ValueError:
        print(f'Formato inválido, {nome} utilize apenas números reais')

c1.comprar(valor)
