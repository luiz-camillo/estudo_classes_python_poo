




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
                print('Livro indisponível')
            counter += 1

l1 = Livros('A Serpente',  'Eduarda Ferreira', 512, False)
l2 = Livros('Sai Azar', 'Luide', 15, True)


biblioteca = Biblioteca()
biblioteca.adicionar_livros(l1)
biblioteca.adicionar_livros(l2)

biblioteca.listar_livros()