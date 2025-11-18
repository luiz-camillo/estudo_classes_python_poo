#programa para calcular area que uma quantidade de tinta rende


#usuario vai informar - rendimento - altura - largura

# o programa vai ter que mostrar vc necessita de x latas de tintas
import math


rendimento = float(input('Quantos metros quadrados de pintura rende a lata de tinta?: '))
altura = float(input('\nQual a altura da parede?: '))
largura = float(input('\nQual a largura da parede?: '))

def calcular_lata(rendimento, altura, largura):
    area = altura * largura
    total_latas = math.ceil(area / rendimento)
    print(f'Você vai precisar de {total_latas} latas de tinta para cobrir a àrea {area}m²')


calcular_lata(rendimento, altura, largura)