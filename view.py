import controller

while True:
    print()
    print("|---------Seja bem vindo--------|")
    print("|--------------Menu-------------|")
    print("|1 - Cadastrar usuário          |")
    print("|2 - Listar usuários cadastrados|")
    print("|3 - Atualizar cadastro         |")
    print("|4 - Excluir cadastro           |")
    print("|0 - Sair                       |")
    print()

    opcao = int(input("Opção: "))

    if opcao == 1:
        controller.cadastrar()

    elif opcao == 2:
        controller.listar()

    elif opcao == 3:
        controller.atualizar()

    elif opcao == 4:
        controller.excluir()

    elif opcao == 0:
        controller.fecharconexao()
        break

    else:
        print("Opção inválida! Tente")
