

class Pessoa:
    def __init__ (self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cargo: {self.cargo}')
        print('\n')

    def promover(self, novo_cargo):
        print(f'{self.nome} foi promovido(a) para a nova função de {novo_cargo}!')
        print('\n')

    def atualizar_idade(self, nova_idade):
        if nova_idade > self.idade:
            print(f'Atualizando a idade de {self.idade} para {nova_idade}')
        else:
            print(f'A nova idade precisa ser maior que a antiga')

pessoa1 = Pessoa('Rafael', 23,'Analista de Redes')

pessoa1.informacoes()
pessoa1.atualizar_idade(21)
pessoa1.promover('Diretor')

