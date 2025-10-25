#polimorfismo

class Personagens:
    def falar(self):
        print('Eu sou um personagem')

class Guerreiro(Personagens):
    def falar(self):
        print('Eu sou um guerreiro forte e destemido!')

class Mago(Personagens):
    def falar(self):
        print('Eu sou um mago sábio e poderoso!')

class Arqueiro(Personagens):
    def falar(self):
        print('Eu sou um arqueiro ágil e letal')



#criar objetos

#personagens = [Guerreiro(), Mago(), Arqueiro()]
#for p in personagens:
#    p.falar()


class Cachorro:
    def emitir_som(self):
        print('AU AU AU AU AU AU AU')

class Gato:
    def emitir_som(self):
        print('MIAAAAAAAAAAAAAAAUU MIAAAUUUU CARAIO')


animais = [Cachorro(),Gato()]

for animal in animais:
    animal.emitir_som()