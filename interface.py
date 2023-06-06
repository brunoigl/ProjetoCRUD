import bancodados

conn = bancodados.conectar_no_banco()
while True:
    print("|---------Seja bem vindo--------|")
    print("|--------------Menu-------------|")
    print("|1 - Cadastrar usuário          |")
    print("|2 - Listar usuários cadastrados|")
    print("|3 - Atualizar cadastro         |")
    print("|4 - Excluir cadastro           |")
    print("|0 - Sair                       |")
    opcao = int(input("\nSelecione uma das opções acima: "))
    if opcao == 1:
        nome, cpf, telefone = bancodados.recebe_dados()
        bancodados.cadastrar(conn, nome, cpf, telefone)
        cadastros = bancodados.ler_cadastros(conn)
        for i in cadastros:
            print(i)
        break
    elif opcao == 2:
        cadastros = bancodados.ler_cadastros(conn)
        for i in cadastros:
            print(f'Código: {i[0]}, Nome: {i[1]}, CPF: {i[2]}, Telefone: {i[3]}')

        break
