import random
import time

guest = random.randint(1,12558848)

print(f'Sejá bem vindo, visitante nº{guest}!')

while True:
    try:
        name = input("Qual é o seu nome?: ").strip()
        if not name:
            raise ValueError("Você não digitou nada!")

        # verifica se todas as palavras têm apenas letras
        palavras = name.split()
        if not all(palavra.isalpha() for palavra in palavras):
            raise ValueError("O nome não pode conter números ou símbolos!")

        break
    except ValueError as e:
        print(f"Erro: {e}. Tente novamente.\n")

print('CARREGANDO ----- ', end=" ")

for n in range(1, 7):
    print(n, end=" ")
    time.sleep(0.4)

for j in range (7, 11):
    print(j, end=" ")
    time.sleep(1)


print('\n \nCarregamento concluído com sucesso! ')
print(f'{name} é muito bom ter você aqui!\n')
time.sleep(0.5)

print(f'Sou Lancaster, seu assistente, hoje minha missão será ajudar você, {name}, a organizar seu tempo!')

while True:
    try:
        tarefas = int(input(f'Me diga, quantas tarefas você quer executar no dia de hoje: '))
        break
    except ValueError:
        print('Digite apenas números inteiros. Tente novamente!\n')

lista_tarefas = []

for i in range(tarefas):
    tarefa =  input(f'Digite o nome da {i+1}ª tarefa: ')
    lista_tarefas.append(tarefa)

print('\n')

tempo_lista = []
for tarefa in lista_tarefas:
    while True:
        try:
            tempo = int(input(f'Digite em minutos o tempo estimado para a tarefa "{tarefa}": '))
            if tempo <= 0:
                raise ValueError("O tempo deve ser maior que zero!")
            tempo_lista.append(tempo)
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.\n")

soma = sum(tempo_lista)
horas = soma // 60
minutos = soma % 60

print(f'\nCom base nas informações inseridas, você vai levar aproximadamente {horas}h {minutos}min para concluir suas tarefas!\n')
print("Dica: tente organizar as tarefas mais importantes primeiro para otimizar seu dia! 🚀")



