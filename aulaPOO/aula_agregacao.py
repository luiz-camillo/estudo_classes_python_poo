

class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.potencia = potencia

class Carro:
    def __init__(self):
        self.motores = []
    def adicionar_motor(self, motor):
        self.motores.append(motor)
    def listar_motor(self):
        for motor in self.motores:
            print(f'Motor marca: {motor.marca} tem a potência de {motor.potencia} cavalos!')
#criando objetos da classe Motor

m1_V6 = Motor('BMW', 350)
m2_v8 = Motor('MERCEDES', 700)
m3_v12 = Motor('FERRARI', 1200)

#criar carro e adicionar motor
c1 = Carro()
c1.adicionar_motor(m1_V6)
c1.listar_motor()

c2 = Carro()
c2.adicionar_motor(m2_v8)
c2.listar_motor()

c3= Carro()
c3.adicionar_motor(m3_v12)
c3.listar_motor()




