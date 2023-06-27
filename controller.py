from time import sleep
import model


def cadastrar():
    nome = str(input("Digite o nome: "))
    cpf = str(input("CPF: "))
    telefone = str(input("Telefone: "))
    res = model.cadastrar_bd(nome, cpf, telefone)
    if res == 1:
        print("Cadastro realizado com sucesso!")
        print(f"Seja bem vindo {nome}")
    else:
        print("Erro ao cadastrar!")


def listar():
    registros = model.lercadastros_bd()
    print("Clientes cadastrados: ")
    for i in registros:
        print(f'Código: {i[0]}\nNome: {i[1]}\nCPF: {i[2]}\nTelefone: {i[3]}')
        print("--------------------------------")


def atualizar():
    cpf = str(input("Informe o CPF do usuário que deseja atualizar: "))
    res = model.buscacadastro_bd(cpf)
    if res == 1:
        nome = str(input("Digite o nome: "))
        telefone = str(input("Telefone: "))
        res = model.atualizacadastro_bd(cpf, nome, telefone)
        if res == 1:
            print("Cadastro Atualizado!")
        else:
            print("Erro ao atualizar o cadastro!")


def excluir():
    cpf = str(input("Informe o CPF do usuário que deseja excluir: "))
    res = model.excluicadastro_bd(cpf)
    if res == 1:
        print("Cadastro Excluído com sucesso!")
    else:
        print("Erro ao excluir cadastro!")


def fecharconexao():
    print("Sistema encerrando...")
    sleep(2)
    model.fecharconexao_bd()
    print("Sistema encerrado!")
    print()
