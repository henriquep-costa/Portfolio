import sqlite3

con = sqlite3.connect('clientes.db')
cur = con.cursor()

# Criação da tabela clientes
cur.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        telefone TEXT,
        tipo TEXT
    )
''')
con.commit()

# Função para adicionar cliente
def adicionar():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    tipo = input("Tipo: ")

    cur.execute('INSERT INTO clientes (nome, telefone, tipo) VALUES (?, ?, ?)',
                (nome, telefone, tipo))
    con.commit()
    print('Cliente salvo.\n')

# Função para listar clientes
def listar():
    cur.execute('SELECT * FROM clientes')
    dados = cur.fetchall()

    print('\n--- CLIENTES ---')
    for c in dados:
        print(f'ID {c[0]} | {c[1]} - {c[2]} ({c[3]})')
    print('-----------------\n')

# Função para deletar cliente
def deletar():
    listar()
    id_cliente = input('Digite o ID do cliente que deseja deletar: ')
    cur.execute('DELETE FROM clientes WHERE id = ?', (id_cliente,))
    con.commit()
    print("Cliente deletado.\n")

# Função para atualizar cliente
def atualizar():
    listar()
    id_cliente = input('ID do cliente que deseja atualizar: ')
    novo_nome = input('Novo nome: ')
    novo_tel = input('Novo telefone: ')
    novo_tipo = input('Novo tipo: ')

    cur.execute('''
        UPDATE clientes
        SET nome = ?, telefone = ?, tipo = ?
        WHERE id = ?
    ''', (novo_nome, novo_tel, novo_tipo, id_cliente))
    con.commit()
    print('Cliente atualizado.\n')

# Menu interativo
def menu():
    while True:
        print("1 - Adicionar cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Deletar cliente")
        print("5 - Sair")

        opcao = input('Escolha: ')

        if opcao == '1':
            adicionar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            atualizar()
        elif opcao == '4':
            deletar()
        elif opcao == '5':
            break
        else:
            print('Opção inválida.\n')

# Executa o menu
menu()
con.close()
