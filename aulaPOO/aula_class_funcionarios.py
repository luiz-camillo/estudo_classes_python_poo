from datetime import datetime

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        print(f'Meu nome é {self.nome} {self.sobrenome}')

    def idade_atual(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        print(f'Eu tenho {self.ano_nascimento} anos')


f1 = Funcionarios('Luiz', 'Ferreira',1996)
f1.nome_completo()
f1.idade_atual()