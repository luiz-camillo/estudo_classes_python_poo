#sistema escola

#Classe Pai

class Pessoas:
    def __init__(self, nome, idade, status):
        self.nome = nome
        self.idade = idade
        self.status = status
    def Apresentar(self):
        print(f'Meu nome é {self.nome} e tenho {self.idade} anos!')
    def statusp(self,status):
        self.status = status
        if self.status:
            print('Essa pessoa está ativa na escola')
        else:
            print('Essa pessoa está inativa na escola')

class Aluno(Pessoas):
    def __init__(self, nome, idade, status, turma):
        super().__init__(nome, idade, status)
        self.turma = turma
    def Apresentar(self):
        super().Apresentar()
        print(f'Meu nome é {self.nome} e tenho {self.idade} anos, sou aluno da turma {self.turma}!')


class Professor(Pessoas):
    def __init__(self, nome, idade, status, materia):
        super().__init__(nome, idade, status)
        self.materia = materia

class Assistente(Pessoas):
    def __init__(self, nome, idade, status, bloco):
        super().__init__(nome, idade, status)
        self.bloco = bloco

a1 = Aluno('Luiz', 15, True,302)
p1 = Professor('Leticia', 28, True,'História')
as1 = Assistente('Luiza', 18, False, 'C')

a1.Apresentar()
p1.Apresentar()
as1.Apresentar()

a1.statusp(True)