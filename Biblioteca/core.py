

import json
import os   

def load_books(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as f:
            try:
                livros = json.load(f)
                return livros
            except json.JSONDecodeError:
                return []
    else: 
        return []

def add_books(nome_arquivo,titulo,autor):
    livros = load_books(nome_arquivo)
    livros.append({"titulo": titulo, "autor": autor})
    with open(nome_arquivo, "w") as f:
        json.dump(livros, f, indent=4)
    return livros  

        