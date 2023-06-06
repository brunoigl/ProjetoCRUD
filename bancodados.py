import firebirdsql as fdb


def solicitar_caminho_banco_dados():
    caminho = input("Digite o caminho do banco de dados Firebird: ")
    return caminho


def conectar_no_banco():
    try:
        conn = fdb.connect(
            host='localhost',
            database=r'C:\Infopoint\InfoPoint ERP-147\BaseDados\Carloni\INFOPOINTERP.FDB',
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


# Consultas

def ler_condicoespgto(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CAD_CONDPAGTMO P ORDER BY P.CPAG_ID")
        registros = cursor.fetchall()
        return registros
    except fdb.Error as erro:
        print("Erro ao ler os registros:", erro)
        return []


def fechar_conexao(conn):
    if conn:
        conn.close()
        print('Conexão encerrada!')
