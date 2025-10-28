




class Livros:
    def __init__(self, titulo, autor, paginas, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponibilidade = disponibilidade

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livros(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        counter = 1
        for livro in self.livros:
            print(f'O {counter}° livro se chama {livro.titulo}, do autor {livro.autor} e possui {livro.paginas} páginas!')
            if livro.disponibilidade:
                print('Livro disponível para venda')
            else:
                print('Livro indisponível para venda')
            counter += 1


titulo = input('Digite o título do livro: ')
autor = input('Digite o nome do autor: ')

while True:
    try:
        paginas = int(input('Quantas páginas tem o livro?: '))
        break
    except ValueError:
        print('Entrada inválida, apenas números inteiros, tente novamente.')

while True:
        disponivel = input('O livro está disponível para venda? (S/N): ').lower()
        if disponivel == 'n' or disponivel== 's':
            break
        else:
            print('Entrada inválida, tente novamente')

if disponivel == 's':
    disponibilidade = True
else:
    disponibilidade = False


l1 = Livros(titulo,  autor, paginas, disponibilidade)

biblioteca = Biblioteca()
biblioteca.adicionar_livros(l1)
biblioteca.listar_livros()


