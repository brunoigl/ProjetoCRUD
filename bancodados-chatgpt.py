import fdb


def conectar_banco_dados(caminho_banco_dados, usuario, senha):
    try:
        conn = fdb.connect(
            dsn=caminho_banco_dados,
            user=usuario,
            password=senha
        )
        return conn
    except fdb.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None


def criar_registro(conn, campo1, campo2):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tabela (campo1, campo2) VALUES (?, ?)", (campo1, campo2))
        conn.commit()
    except fdb.Error as e:
        print("Erro ao criar o registro:", e)


def ler_registros(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tabela")
        registros = cursor.fetchall()
        return registros
    except fdb.Error as e:
        print("Erro ao ler os registros:", e)
        return []


def atualizar_registro(conn, id_registro, campo1, campo2):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE tabela SET campo1 = ?, campo2 = ? WHERE id = ?",
                       (campo1, campo2, id_registro))
        conn.commit()
    except fdb.Error as e:
        print("Erro ao atualizar o registro:", e)


def deletar_registro(conn, id_registro):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tabela WHERE id = ?", (id_registro,))
        conn.commit()
    except fdb.Error as e:
        print("Erro ao deletar o registro:", e)


def fechar_conexao(conn):
    if conn:
        conn.close()
        print("Conexão fechada.")
