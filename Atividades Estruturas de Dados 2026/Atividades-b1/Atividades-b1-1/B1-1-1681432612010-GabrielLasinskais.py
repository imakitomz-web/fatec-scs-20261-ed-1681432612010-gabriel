'''
 ---------------------------------------------------------------------------
                FATEC São Caetano do Sul
		  Atividade B1 - 1  
 Autor: 1681432612010 - Gabriel Lasinskais
 Objetivo: Executar operações de cadastro, busca, remoção e listagem de filmes 
 Data:24/02/2026
  ---------------------------------------------------------------------------
'''
catalogo = {}
def adicionar_filme(id_filme, titulo, diretor):
            if id_filme not in catalogo:
                catalogo[id_filme] = {"ID:":id_filme, "Título:":titulo, "Diretor:": diretor}
            else:
                print("ID já existe")

def buscar_filme(id_filme):
    return catalogo.get(id_filme, "Filme não encontrado")
#"""Consulta um filme usando o m todo seguro .get()."""
def remover_filme(id_filme):
    catalogo.pop(id_filme)
#"""Remove um filme do dicion rio usando .pop()."""
def listar_todos():
    if not catalogo:
        print("\nO catalogo esta vazio.")
    else:
        print(catalogo)
    for id_filme, dados in catalogo.items():
        print("ID: {id_filme} | Titulo: {dados[’titulo’]} | Diretor: {dados[’diretor’]}")




adicionar_filme(1, "Matrix", "Eu")
adicionar_filme(2, "Vingadores", "Bah")