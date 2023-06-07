import firebirdsql as fdb


def conectar_no_banco():
    try:
        conn = fdb.connect(
            host='localhost',
            database=r'D:\ProjetosPython\ProjetoCRUD\VALHALLA.FDB',
            port=3050,
            user='SYSDBA',
            password='info0710'
        )
    except fdb.Error as erro:
        print(f'ERRO! \n {erro}')
        return None
    else:
        print('\nConexão realizada com sucesso!\n')
        return conn

# Chama o menu de opções e retorna a opção escolhidaa


def menu():
    print()
    print("|---------Seja bem vindo--------|")
    print("|--------------Menu-------------|")
    print("|1 - Cadastrar usuário          |")
    print("|2 - Listar usuários cadastrados|")
    print("|3 - Atualizar cadastro         |")
    print("|4 - Excluir cadastro           |")
    print("|0 - Sair                       |")
    print()


def ler_cadastros(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CLIENTE C ORDER BY C.CLI_ID")
        registros = cursor.fetchall()
        print("Clientes cadastrados: ")
        for i in registros:
            print(f'Código: {i[0]}, Nome: {i[1]}, CPF: {i[2]}, Telefone: {i[3]}')
        print()
    except fdb.Error as erro:
        print(f"Erro ao ler os registros: {erro}")
        return 0


def recebe_dados():
    print("---Cadastro de usuário---")
    nome = str(input("Digite o nome: "))
    cpf = str(input("Digite o CPF: "))
    telefone = str(input("Digite o telefone: "))
    return nome, cpf, telefone


def cadastrar(conn, cli_nome, cli_cpf, cli_telefone):
    try:
        cursor = conn.cursor()
        query = "insert into cliente (cli_nome, cli_cpf, cli_telefone) values (?, ?, ?)"
        cursor.execute(query, (cli_nome, cli_cpf, cli_telefone))
        conn.commit()
    except fdb.Error as erro:
        print(f"Erro ao inserir registros: {erro}")


def atualiza_cadastro(conn, cli_cpf, cli_nome, cli_telefone):
    try:
        cursor = conn.cursor()
        query = "UPDATE cliente SET cli_nome = ?, cli_telefone = ? WHERE cli_cpf = ?"
        cursor.execute(query, (cli_nome, cli_telefone, cli_cpf))
        conn.commit()
    except fdb.Error as erro:
        print(f"Erro ao atualizar cadastro: {erro}")


def exclui_cadastro(conn, cpf):
    try:
        cursor = conn.cursor()
        query = "delete from cliente where cli_cpf = ?"
        cursor.execute(query, (cpf,))
        conn.commit()
    except fdb.Error as erro:
        print(f'Erro ao excluir cadastro {erro}')


def fechar_conexao(conn):
    if conn:
        conn.close()
        print('Sistema encerrado!')
