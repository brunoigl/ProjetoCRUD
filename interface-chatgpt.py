import database

def exibir_menu():
    print("==== CRUD App ====")
    print("1. Criar registro")
    print("2. Ler registros")
    print("3. Atualizar registro")
    print("4. Deletar registro")
    print("0. Sair")

def obter_dados_registro():
    # Função auxiliar para obter os dados de um registro do usuário
    # Nesse exemplo, supomos que o registro é composto por dois valores: campo1 e campo2
    campo1 = input("Digite o valor do campo1: ")
    campo2 = input("Digite o valor do campo2: ")
    return campo1, campo2

def executar():
    # Estabelecer conexão com o banco de dados
    conn = database.conectar_banco_dados()
    if not conn:
        return

    while True:
        exibir_menu()
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            campo1, campo2 = obter_dados_registro()
            database.criar_registro(conn, campo1, campo2)
            print("Registro criado com sucesso!")

        elif opcao == "2":
            registros = database.ler_registros(conn)
            print("Registros:")
            for registro in registros:
                print(registro)

        elif opcao == "3":
            id_registro = input("Digite o ID do registro a ser atualizado: ")
            campo1, campo2 = obter_dados_registro()
            database.atualizar_registro(conn, id_registro, campo1, campo2)
            print("Registro atualizado com sucesso!")

        elif opcao == "4":
            id_registro = input("Digite o ID do registro a ser deletado: ")
            database.deletar_registro(conn, id_registro)
            print("Registro deletado com sucesso!")

        elif opcao == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")

    # Fechar conexão com o banco de dados
    database.fechar_conexao(conn)

# Executar a aplicação
if __name__ == "__main__":
    executar()
