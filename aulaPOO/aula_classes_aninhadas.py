


#Classe Main

class Computador:
    def __init__(self, modelo, ram_gb, processador):
        self.modelo = modelo
        self.ram_gb = ram_gb
        self.processador = processador

    def mostrarconf(self):
        print(f'Computador: {self.modelo} - {self.ram_gb}GB RAM - Processador: {self.processador}')


    class GPU:
        def __init__(self, nome, memoria_gb):
            self.nome = nome
            self.memoria_gb = memoria_gb

        def mostrarGPU(self):
            print(f'GPU: {self.nome} - {self.memoria_gb}GB')


#utilizacao 

pc1 = Computador('Samsung BOOK', 12, 'INTEL I5')
gpu1 = Computador.GPU('NVIDIA RTX 5090', 24)
pc1.mostrarconf()
gpu1.mostrarGPU()



