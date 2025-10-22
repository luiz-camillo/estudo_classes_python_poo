
#criar a classe - nome de classe precisa começar com letra maiuscula
class Funcionarios:
    pass

#criando objeto
userOne = Funcionarios()
userTwo = Funcionarios()

#criar parametros usuario one
userOne.name = 'Luiz'
userOne.surname = 'Camillo'
userOne.birthday = '09/11/1996'

#criar parametros usuario two
userTwo.name = 'Duda'
userTwo.surname = 'Camillo'
userTwo.birthday = '18/12/1997'



print(userOne.surname)
print(userTwo.surname)
print(userOne.name)
print(userTwo.birthday)

