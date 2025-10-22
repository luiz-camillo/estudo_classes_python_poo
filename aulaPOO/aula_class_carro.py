class Carro:
    def __init__(self, cor, ano ):
        self.cor = cor
        self.ano = ano
        self.ligado = True
        self.seta = None

    def info (self):
        print(f'A cor do carro é {self.cor} e ele foi fabricado no ano {self.ano}')

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('O carro está ligado')
        else:
            print('O carro já estava ligado')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('O carro foi desligado')
        else:
            print('O carro estava desligado')

    def ligar_seta(self, direcao):
        if not self.ligado:
            print('Ligue o carro para utilizar seta')
        else:
            self.seta = direcao
            print(f'Seta ligada para a {self.seta}')


carro1 = Carro('Preto',2021)
carro1.info()
carro1.desligar()
carro1.ligar_seta('direita')