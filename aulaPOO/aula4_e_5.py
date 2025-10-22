

class Funcionarios:
    def __init__(self, name, surname, birthday):
        self.name = name
        self.surname = surname
        self.birthday = birthday
    def full_name(self):
        return self.name + ' ' + self.surname


#criar objeto
usuario1 = Funcionarios('Luiz','Ferreira','09/11/1996')
usuario2 = Funcionarios('Eduarda', 'Ferreira', '18/12/1997')
usuario3 = Funcionarios('Dieison', 'Oliveira', '15/01/1998')

#print
print(usuario1.surname)
print(usuario2.name)
print(usuario3.birthday)

#quero imprimir nome e sobrenome do usuario1

print('Imprimindo nome completo da tigrada com função nome completo dentro da classe')
print(usuario1.full_name())
print(Funcionarios.full_name(usuario3))