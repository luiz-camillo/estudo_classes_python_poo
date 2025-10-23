#heranca multipla e heranca multinivel

#Classes pai

class Animal:
    def __init__(self, nome):
        self.nome = nome

#Classes filhas

class Predador(Animal):
    def cacando(self):
        print(f'O animal {self.nome} está caçando!')

class Presa(Animal):
    def fugindo(self):
        print(f'O animal {self.nome} está fugindo!')

#Classes netas

class Coelho(Presa):
    pass

class Tigre(Predador):
    pass

class Golfinho(Predador, Presa):
    pass

#coelho1 = Coelho('Lambisgoio')
#tigre1 = Tigre('Dentinho')
#golfinho1 = Golfinho('Bichano')

#coelho1.fugindo()
#tigre1.cacando()
#golfinho1.cacando()

#### estudo de novas classes


#Classe pai

class Funcionarios:
    def __init__(self, nome, idade, nr_cadastro):
        self.nome = nome
        self.idade = idade
        self.nr_cadastro = nr_cadastro

#Classes filhas

class Diretoria(Funcionarios):
    def __init__(self, nome, idade, nr_cadastro, setorgestao):
        super().__init__(nome, idade, nr_cadastro)
        self.setorgestao = setorgestao
    def apresentar(self):
        print(f'Olá, meu nome é {self.nome
        }, tenho {self.idade} anos, meu Nr de Registro na empresa é {self.nr_cadastro} e sou gestor do setor de {self.setorgestao}')
    def trabalhar(self):
        print('Estou trabalhando')

class OreiaSeca(Funcionarios):
    def __init__(self, nome, idade, nr_cadastro, funcao):
        super().__init__(nome, idade, nr_cadastro)
        self.funcao = funcao
    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}, tenho {self.idade} anos, meu Nr de registro na empresa é {self.nr_cadastro} e trabalho na função de {self.funcao}')
    def trabalhar(self):
        print('Estou trabalhando')


d1 = Diretoria('Luiz', 28, 1233, 'Desenvolvimento de Software')
f1 = OreiaSeca('Gerson', 21, 551515, 'Desenvolvedor .NET')

d1.apresentar()
f1.apresentar()