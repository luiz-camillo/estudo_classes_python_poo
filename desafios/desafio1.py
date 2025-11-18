#programa vai gerar 3 listas

#lista 1 de funcionarios que tem carros e trabalham a noite

#lista 2 de funcionarios que tem carros e trabalham de dia

#lista 3 de funcionarios que nao tem carros

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']

turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']

turno_noite = ['Pedro', 'Sophia', 'Bruno']

tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']


#lista1

lista1 = set(tem_carro).intersection(set(turno_noite))
print(lista1)

#lista2
lista2 = set(tem_carro).intersection(set(turno_dia))
print(lista2)

#lista3
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)