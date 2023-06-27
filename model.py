import firebirdsql as fdb


def conectarnobanco():
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
        return conn


def lercadastros_bd():
    conn = conectarnobanco()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CLIENTE C ORDER BY C.CLI_ID")
        registros = cursor.fetchall()
        return registros
    except fdb.Error as erro:
        print(f"Erro ao ler os registros: {erro}")
        return 0


def buscacadastro_bd(cpf):
    conn = conectarnobanco()
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM CLIENTE WHERE CLIENTE.CLI_CPF = {cpf}")
        registros = cursor.fetchall()
        if len(registros) >= 1:
            return 1
        else:
            print("Não foi localizado usuário cadastrado com esse CPF.")
            return 0
    except fdb.Error as erro:
        print(f"Erro ao atualizar cadastro: {erro}")
        return erro


def cadastrar_bd(cli_nome, cli_cpf, cli_telefone):
    conn = conectarnobanco()
    try:
        cursor = conn.cursor()
        query = "insert into cliente (cli_nome, cli_cpf, cli_telefone) values (?, ?, ?)"
        cursor.execute(query, (cli_nome, cli_cpf, cli_telefone))
        conn.commit()
        return 1
    except fdb.Error as erro:
        print(f"Erro ao inserir registros: {erro}")
        return 0


def atualizacadastro_bd(cli_cpf, cli_nome, cli_telefone):
    conn = conectarnobanco()
    try:
        cursor = conn.cursor()
        query = "UPDATE cliente SET cli_nome = ?, cli_telefone = ? WHERE cli_cpf = ?"
        cursor.execute(query, (cli_nome, cli_telefone, cli_cpf))
        conn.commit()
        return 1
    except fdb.Error as erro:
        print(f"Erro ao atualizar cadastro: {erro}")
        return 0


def excluicadastro_bd(cpf):
    conn = conectarnobanco()
    try:
        cursor = conn.cursor()
        query = "delete from cliente where cli_cpf = ?"
        cursor.execute(query, (cpf,))
        conn.commit()
        return 1
    except fdb.Error as erro:
        print(f'Erro ao excluir cadastro {erro}')
        return 0


def fecharconexao_bd():
    conn = conectarnobanco()
    if conn:
        conn.close()
