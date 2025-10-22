

class Casa:
    def __init__(self, cor, quartos, banheiro):
        self.cor = cor
        self.quartos = quartos
        self.banheiro = banheiro
    def mostrar_cor(self):
        return f'A cor da da casa é {self.cor}'
    def mostrar_quartos(self):
        return f'Essa casa tem {self.quartos} quartos'
    def mostrar_banheiro(self):
        return f'Essa casa tem {self.banheiro} banheiros'
    def adicionar_quarto(self):
        self.quartos = self.quartos + 1
        return f'Esta casa tem {self.quartos} quartos'
    def pintar(self, nova_cor):
        antiga = self.cor
        self.cor = nova_cor
        return f'Esta casa foi pintada, ela tinha a cor {antiga} e agora está pintada de {self.cor}'

casa1 = Casa('Azul',3,2)
print(Casa.mostrar_cor(casa1))
print(Casa.adicionar_quarto(casa1))
print(Casa.mostrar_banheiro(casa1))
print(Casa.pintar(casa1,'Preto',))
print(Casa.mostrar_cor(casa1))