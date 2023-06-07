import bancodados
from time import sleep


conn = bancodados.conectar_no_banco()
while True:

    bancodados.menu()
    opcao = int(input("\nSelecione uma das opções acima: "))
    print()

    if opcao == 1:
        nome, cpf, telefone = bancodados.recebe_dados()
        bancodados.cadastrar(conn, nome, cpf, telefone)
        print()
        print(f'{nome} cadastrado com sucesso.')
        sleep(2)

    elif opcao == 2:
        CADASTROS = bancodados.ler_cadastros(conn)

    elif opcao == 3:
        CPF = str(input('Informe o CPF do cadastro que deseja atualizar: '))
        NOME = str(input('Atualize o NOME do cliente: '))
        TELEFONE = str(input('Atualize o TELEFONE do cliente: '))
        bancodados.atualiza_cadastro(conn, CPF, NOME, TELEFONE)
        CADASTROS = bancodados.ler_cadastros(conn)

    elif opcao == 4:
        CPF = str(input('Informe o CPF do cadastro que deseja excluir: '))
        bancodados.exclui_cadastro(conn, CPF)
        CADASTROS = bancodados.ler_cadastros(conn)
        print("Cadastro excluído com sucesso!")

    elif opcao == 0:
        break

    else:
        print("Opção inválida. Tente novamente.")

bancodados.fechar_conexao(conn)
