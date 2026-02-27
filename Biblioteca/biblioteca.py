

import json
import os   


def menu():
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Sair")

def adicionar_livro(livros):
    titulo = input("Digite o título do livro lido: ")
    autor = input("Digite o autor do livro: ")
    livros.append({"titulo": titulo, "autor": autor})
    print("Livro adicionado com sucesso!")

def listar_livros(livros):
    if not livros:
        print("Nenhum livro registrado.")
    else:
        print("Livros lidos:")
        for idx, livro in enumerate(livros, start=1):
            print(f"{idx}. {livro['titulo']} - {livro['autor']}")

def main():
    if os.path.exists("biblioteca.json"):
        with open('biblioteca.json', 'r') as f:
            try:
                livros = json.load(f)
            except json.JSONDecodeError:
                livros = []
    else:
        livros = []
    while True:
        menu()
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_livro(livros)
        elif escolha == '2':
            listar_livros(livros)
        elif escolha == '3':
            with open('biblioteca.json', 'w') as f:
                json.dump(livros, f, indent=4)
            print("Saindo da biblioteca. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")     

if __name__ == "__main__": 
    main()       