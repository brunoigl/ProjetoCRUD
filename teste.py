import firebirdsql as fdb

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

def criar_registro(conn, tabela, registro):
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO {tabela} VALUES ({registro})")
        conn.commit()
        print("Registro criado com sucesso!")
    except fdb.Error as e:
        print("Erro ao criar o registro:", e)

def ler_registros(conn, tabela):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {tabela}")
        registros = cursor.fetchall()
        return registros
    except fdb.Error as e:
        print("Erro ao ler os registros:", e)
        return []

def atualizar_registro(conn, tabela, indice, novo_registro):
    try:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {tabela} SET coluna = {novo_registro} WHERE id = {indice}")
        conn.commit()
        print("Registro atualizado com sucesso!")
    except fdb.Error as e:
        print("Erro ao atualizar o registro:", e)

def deletar_registro(conn, tabela, indice):
    try:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {tabela} WHERE id = {indice}")
        conn.commit()
        print("Registro deletado com sucesso!")
    except fdb.Error as e:
        print("Erro ao deletar o registro:", e)

def fechar_conexao(conn):
    if conn:
        conn.close()

def exibir_menu():
    print("==== CRUD App ====")
    print("1. Criar registro")
    print("2. Ler registros")
    print("3. Atualizar registro")
    print("4. Deletar registro")
    print("0. Sair")

def executar():
    caminho = "caminho/para/banco_de_dados.fdb"
    usuario = "seu_usuario"
    senha = "sua_senha"
    tabela = "nome_da_tabela"

    conn = conectar_banco_dados(caminho, usuario, senha)
    if not conn:
        return

    while True:
        exibir_menu()
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            registro = input("Digite o novo registro: ")
            criar_registro(conn, tabela, registro)

        elif opcao == "2":
            registros = ler_registros(conn, tabela)
            print("Registros:")
            for indice, registro in registros:
                print(f"{indice}: {registro}")

        elif opcao == "3":
            indice = int(input("Digite o índice do registro a ser atualizado: "))
            novo_registro = input("Digite o novo valor do registro: ")
            atualizar_registro(conn, tabela, indice, novo_registro)

        elif opcao == "4":
            indice = int(input("Digite o índice do registro a ser deletado: "))
            deletar_registro(conn, tabela, indice)

        elif opcao == "0":
            fechar_conexao(conn)
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar a aplicação
if __name__ == "__main__":
    executar()