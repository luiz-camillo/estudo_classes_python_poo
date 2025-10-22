


class Animal:
    def __init__ (self, nome, cor, raca):
        self.nome = nome
        self.cor = cor
        self.raca = raca

    def apresentar(self):
        print(f'Eu sou o {self.raca}, me chamo {self.nome} e minha cor é {self.cor}')

    def soltar(self, status):
        print('Soltando o animal...... ')
        if status == 'Solto':
            print('O animal já estava solto')
        else:
            print('O animal acabou de ser solto')



class Gato(Animal):
    def miar(self):
        print('miau')
    def arranhar(self):
        print('O gato está arranhando')

class Cachorro(Animal):
    def latir(self):
        print('au au')
    def morder(self):
        print('O cachorro está mordendo')

class Elefante(Animal):
    def trumpetar(self):
        print('bruuuuh')

gato1 = Gato('Felix','Branco', 'Gato Persa')
gato1.apresentar()
gato1.miar()
gato1.arranhar()
gato1.soltar('Preso')
