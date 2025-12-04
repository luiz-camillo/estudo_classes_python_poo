s1 = {'joao', 'marcela', 'benicio', 'eduarda', 'luiz'}
s2 = {'marcos', 'alex', 'marcela', 'luiz', 'toninho'}
s3 = {'toninho', 'luiz', 'leocir', 'arthur', 'claudia'}


repetidos = s1.intersection(s2,s3)
todosunidossemrepetir = s1.union(s2,s3)
diferenca = {nome for nome in todosunidossemrepetir if
             sum(nome in s for s in [s1, s2, s3]) == 1}

print(f'Os nomes repetidos nas 3 listas são: {repetidos} ')
print(f'Todos os nomes desconsiderado os repetidos são: {todosunidossemrepetir}')
print(f'Esse são os nomes que só aparecem uma única vez nas listas: {diferenca}')