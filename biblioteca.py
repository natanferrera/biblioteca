import math
import matplotlib.pyplot as plt

#criando ecossistema
class Livro:
    def __init__(self, titulo, genero, autor, ano_publicacao):
        self.titulo = titulo
        self.genero = genero
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"Titulo: {self.titulo} Gênero: {self.genero} por {self.autor} Publicado em {self.ano_publicacao}"

    def __repr__(self):
        return f"titulo'{self.titulo}', Gênero:'{self.genero}', Autor:'{self.autor}', Publicado em:'{self.ano_publicacao})'"


biblioteca = []
anos = []
generos = []


# Função para adicionar um livro à biblioteca com input
def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    genero = input("Digite o gênero do livro: ")
    autor = input("Digite o autor do livro: ")
    ano_publicacao = int(input("Digite o ano de publicação do livro: "))

    # Criando um objeto do livro
    novo_livro = Livro(titulo, genero, autor, ano_publicacao)
    biblioteca.append(novo_livro)
    anos.append(ano_publicacao)
    generos.append(genero)

    print(f"\n{titulo} adicionado com sucesso!")

#função que adiciona lista de livros que já foram criados:
def inserir_livro(titulo, genero, autor, ano_publicacao):
  novo_livro = Livro(titulo, genero, autor, ano_publicacao)
  biblioteca.append(novo_livro)
  anos.append(ano_publicacao)
  generos.append(genero)
  print(f"\n{titulo} de {genero}, adicionado com sucesso!")

inserir_livro("1984", "Ficção Científica", "George Orwell", 1949)
inserir_livro("Dom Quixote", "Romance", "Miguel de Cervantes", 1605)
inserir_livro("Orgulho e Preconceito", "Romance", "Jane Austen", 1813)
inserir_livro("O Senhor dos Anéis", "Fantasia", "J.R.R. Tolkien", 1954)
inserir_livro("Cem Anos de Solidão", "Realismo Mágico", "Gabriel García Márquez", 1967)
inserir_livro("O Pequeno Príncipe", "Fábula", "Antoine de Saint-Exupéry", 1943)
inserir_livro("Crime e Castigo", "Romance Psicológico", "Fiódor Dostoiévski", 1866)
inserir_livro("A Revolução dos Bichos", "Sátira", "George Orwell", 1945)
inserir_livro("Alice no País das Maravilhas", "Fantasia", "Lewis Carroll", 1865)
inserir_livro("A Metamorfose", "Ficção Existencialista", "Franz Kafka", 1915)
inserir_livro("O Grande Gatsby", "Romance", "F. Scott Fitzgerald", 1925)
inserir_livro("Moby Dick", "Aventura", "Herman Melville", 1851)
inserir_livro("O Morro dos Ventos Uivantes", "Romance Gótico", "Emily Brontë", 1847)
inserir_livro("Drácula", "Terror", "Bram Stoker", 1897)
inserir_livro("As Crônicas de Nárnia", "Fantasia", "C.S. Lewis", 1950)
inserir_livro("Fahrenheit 451", "Ficção Científica", "Ray Bradbury", 1953)
inserir_livro("Os Miseráveis", "Romance Histórico", "Victor Hugo", 1862)
inserir_livro("O Nome do Vento", "Fantasia", "Patrick Rothfuss", 2007)
inserir_livro("Neuromancer", "Cyberpunk", "William Gibson", 1984)
inserir_livro("A Fundação", "Ficção Científica", "Isaac Asimov", 1951)

#listar livros
def listar_livros():
  print("Livros na biblioteca:")
  for livro in biblioteca:
    print(livro)

listar_livros()

#criar um gráfico listando livros por ano
anos = list(set(anos))# remove duplicatas
anos.sort()

#contagem de livros por ano
contagem_livros = [anos.count(ano) for ano in anos]

generos = list(set(generos))
generos.sort()
contagem_genero = [generos.count(genero) for genero in generos]

#função que busca um livro pelo título
def buscar():
    titulo_pesquisa = input("Digite o título do livro que deseja buscar: ")
    for livro in biblioteca:
        if livro.titulo.lower() == titulo_pesquisa.lower():
            print(f"Livro encontrado: {livro}")
            return livro
    return None

buscar()

#crie um gráfico de pizza de quantidade de livros por gênero sem ser em porcentagem
plt.pie(contagem_genero, labels=generos, autopct='%1.1f%%')
plt.title('Quantidade de Livros por Gênero')
plt.show()