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

# Consulta


def ler_cadastros(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CLIENTE C ORDER BY C.CLI_ID")
        registros = cursor.fetchall()
        return registros
    except fdb.Error as erro:
        print(f"Erro ao ler os registros: {erro}")
        return []


def recebe_dados():
    nome = str(input("Digite o nome: "))
    cpf = str(input("Digite o CPF: "))
    telefone = str(input("Digite o telefone: "))
    return nome, cpf, telefone


def cadastrar(conn, cli_nome, cli_cpf, cli_telefone):
    try:
        cursor = conn.cursor()
        cursor.execute(f"insert into cliente (cli_nome, cli_cpf, cli_telefone) values ('{cli_nome}', '{cli_cpf}', '{cli_telefone}')")
        conn.commit()
    except fdb.Error as erro:
        print(f"Erro ao inserir registros: {erro}")


def fechar_conexao(conn):
    if conn:
        conn.close()
        print('Conexão encerrada!')
