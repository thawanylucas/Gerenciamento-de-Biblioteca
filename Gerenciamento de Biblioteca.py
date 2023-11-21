import pickle
import tkinter as tk
from tkinter import messagebox

class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano_publicacao}), {self.genero}"

class CadastroLivros:
    def __init__(self):
        self.livros = {}

    def cadastrar_livro(self, livro):
        titulo = livro.titulo
        if titulo not in self.livros:
            self.livros[titulo] = livro
            return f"Livro '{titulo}' cadastrado com sucesso!"
        else:
            return f"Erro: Livro '{titulo}' já cadastrado."

    def listar_livros(self):
        lista = []
        for livro in self.livros.values():
            lista.append(str(livro))
        return lista

    def consultar_livro(self, titulo):
        if titulo in self.livros:
            livro = self.livros[titulo]
            return f"Informações sobre o livro '{titulo}':\n{str(livro)}"
        else:
            return f"Livro '{titulo}' não encontrado."

    def listar_livros_por_autor(self, autor):
        livros_do_autor = [livro for livro in self.livros.values() if livro.autor == autor]
        lista = []
        if livros_do_autor:
            lista.append(f"\nLivros do autor '{autor}':")
            for livro in livros_do_autor:
                lista.append(str(livro))
        else:
            lista.append(f"Nenhum livro encontrado para o autor '{autor}'.")
        return lista

    def listar_livros_por_genero(self, genero):
        livros_do_genero = [livro for livro in self.livros.values() if livro.genero == genero]
        lista = []
        if livros_do_genero:
            lista.append(f"\nLivros do gênero '{genero}':")
            for livro in livros_do_genero:
                lista.append(str(livro))
        else:
            lista.append(f"Nenhum livro encontrado para o gênero '{genero}'.")
        return lista

    def salvar_para_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.livros, arquivo)
        return f"Dados salvos no arquivo '{nome_arquivo}'."

    def carregar_de_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'rb') as arquivo:
                self.livros = pickle.load(arquivo)
            return f"Dados carregados do arquivo '{nome_arquivo}'."
        except FileNotFoundError:
            return f"Arquivo '{nome_arquivo}' não encontrado. Nenhum dado carregado."

# interface gráfica
def cadastrar_livro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    ano = entry_ano.get()
    genero = entry_genero.get()

    try:
        ano = int(ano)
    except ValueError:
        messagebox.showerror("Erro", "O ano de publicação deve ser um número inteiro.")
        return

    livro = Livro(titulo, autor, ano, genero)
    resultado = cadastro.cadastrar_livro(livro)
    messagebox.showinfo("Cadastro de Livro", resultado)

def consultar_livro():
    titulo = entry_titulo_consulta.get()
    resultado = cadastro.consultar_livro(titulo)
    messagebox.showinfo("Consulta de Livro", resultado)

def listar_livros_por_autor():
    autor = entry_autor_consulta.get()
    resultado = cadastro.listar_livros_por_autor(autor)
    messagebox.showinfo("Listagem de Livros por Autor", "\n".join(resultado))

def listar_livros_por_genero():
    genero = entry_genero_consulta.get()
    resultado = cadastro.listar_livros_por_genero(genero)
    messagebox.showinfo("Listagem de Livros por Gênero", "\n".join(resultado))

def salvar_dados():
    nome_arquivo = entry_nome_arquivo.get()

    if not nome_arquivo:
        messagebox.showerror("Erro", "Por favor, forneça um nome de arquivo.")
        return

    resultado = cadastro.salvar_para_arquivo(nome_arquivo)
    messagebox.showinfo("Salvar Dados", resultado)

def carregar_dados():
    nome_arquivo = entry_nome_arquivo.get()

    if not nome_arquivo:
        messagebox.showerror("Erro", "Por favor, forneça um nome de arquivo.")
        return

    resultado = cadastro.carregar_de_arquivo(nome_arquivo)
    messagebox.showinfo("Carregar Dados", resultado)

# Configuração
root = tk.Tk()
root.title("Cadastro de Livros")

cadastro = CadastroLivros()

# cadastro de livros
label_titulo = tk.Label(root, text="Título:")
label_titulo.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
entry_titulo = tk.Entry(root)
entry_titulo.grid(row=0, column=1, padx=5, pady=5)

label_autor = tk.Label(root, text="Autor:")
label_autor.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
entry_autor = tk.Entry(root)
entry_autor.grid(row=1, column=1, padx=5, pady=5)

label_ano = tk.Label(root, text="Ano de Publicação:")
label_ano.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
entry_ano = tk.Entry(root)
entry_ano.grid(row=2, column=1, padx=5, pady=5)

label_genero = tk.Label(root, text="Gênero:")
label_genero.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
entry_genero = tk.Entry(root)
entry_genero.grid(row=3, column=1, padx=5, pady=5)

btn_cadastrar = tk.Button(root, text="Cadastrar Livro", command=cadastrar_livro)
btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=10)

# consulta de livros
label_titulo_consulta = tk.Label(root, text="Título:")
label_titulo_consulta.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
entry_titulo_consulta = tk.Entry(root)
entry_titulo_consulta.grid(row=5, column=1, padx=5, pady=5)

btn_consultar = tk.Button(root, text="Consultar Livro", command=consultar_livro)
btn_consultar.grid(row=6, column=0, columnspan=2, pady=10)

# listagem de livros por autor
label_autor_consulta = tk.Label(root, text="Autor:")
label_autor_consulta.grid(row=7, column=0, sticky=tk.W, padx=5, pady=5)
entry_autor_consulta = tk.Entry(root)
entry_autor_consulta.grid(row=7, column=1, padx=5, pady=5)

btn_listar_por_autor = tk.Button(root, text="Listar por Autor", command=listar_livros_por_autor)
btn_listar_por_autor.grid(row=8, column=0, columnspan=2, pady=10)

# listagem de livros por gênero
label_genero_consulta = tk.Label(root, text="Gênero:")
label_genero_consulta.grid(row=9, column=0, sticky=tk.W, padx=5, pady=5)
entry_genero_consulta = tk.Entry(root)
entry_genero_consulta.grid(row=9, column=1, padx=5, pady=5)

btn_listar_por_genero = tk.Button(root, text="Listar por Gênero", command=listar_livros_por_genero)
btn_listar_por_genero.grid(row=10, column=0, columnspan=2, pady=10)

# salvar e carregar dados
label_nome_arquivo = tk.Label(root, text="Nome do Arquivo:")
label_nome_arquivo.grid(row=11, column=0, sticky=tk.W, padx=5, pady=5)
entry_nome_arquivo = tk.Entry(root)
entry_nome_arquivo.grid(row=11, column=1, padx=5, pady=5)

btn_salvar_dados = tk.Button(root, text="Salvar Dados", command=salvar_dados)
btn_salvar_dados.grid(row=12, column=0, pady=10)

btn_carregar_dados = tk.Button(root, text="Carregar Dados", command=carregar_dados)
btn_carregar_dados.grid(row=12, column=1, pady=10)

root.mainloop()