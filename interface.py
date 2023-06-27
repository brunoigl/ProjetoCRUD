import tkinter as tk
from tkinter import messagebox
import model
from time import sleep


def cadastrar():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    telefone = entry_telefone.get()

    model.cadastrar(conn, nome, cpf, telefone)

    messagebox.showinfo("Sucesso", f"{nome} cadastrado com sucesso.")


def atualizar():
    cpf = entry_cpf_atualizar.get()
    nome = entry_nome_atualizar.get()
    telefone = entry_telefone_atualizar.get()

    model.atualiza_cadastro(conn, cpf, nome, telefone)

    messagebox.showinfo("Sucesso", "Cadastro atualizado com sucesso.")


def excluir():
    cpf = entry_cpf_excluir.get()

    model.exclui_cadastro(conn, cpf)

    messagebox.showinfo("Sucesso", "Cadastro excluído com sucesso.")


# Conexão com o banco de dados
conn = model.conectar_no_banco()

# Criação da janela principal
root = tk.Tk()
root.title("Cadastro de Clientes")

# Label e Entry para cadastrar
label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0, sticky=tk.W)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_cpf = tk.Label(root, text="CPF:")
label_cpf.grid(row=1, column=0, sticky=tk.W)
entry_cpf = tk.Entry(root)
entry_cpf.grid(row=1, column=1, padx=10, pady=5)

label_telefone = tk.Label(root, text="Telefone:")
label_telefone.grid(row=2, column=0, sticky=tk.W)
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=2, column=1, padx=10, pady=5)

btn_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar)
btn_cadastrar.grid(row=3, column=0, columnspan=2, pady=10)

# Label e Entry para atualizar
label_cpf_atualizar = tk.Label(root, text="CPF:")
label_cpf_atualizar.grid(row=4, column=0, sticky=tk.W)
entry_cpf_atualizar = tk.Entry(root)
entry_cpf_atualizar.grid(row=4, column=1, padx=10, pady=5)

label_nome_atualizar = tk.Label(root, text="Novo Nome:")
label_nome_atualizar.grid(row=5, column=0, sticky=tk.W)
entry_nome_atualizar = tk.Entry(root)
entry_nome_atualizar.grid(row=5, column=1, padx=10, pady=5)

label_telefone_atualizar = tk.Label(root, text="Novo Telefone:")
label_telefone_atualizar.grid(row=6, column=0, sticky=tk.W)
entry_telefone_atualizar = tk.Entry(root)
entry_telefone_atualizar.grid(row=6, column=1, padx=10, pady=5)

btn_atualizar = tk.Button(root, text="Atualizar", command=atualizar)
btn_atualizar.grid(row=7, column=0, columnspan=2, pady=10)

# Label e Entry para excluir
label_cpf_excluir = tk.Label(root, text="CPF:")
label_cpf_excluir.grid(row=8, column=0, sticky=tk.W)
entry_cpf_excluir = tk.Entry(root)
entry_cpf_excluir.grid(row=8, column=1, padx=10, pady=5)

btn_excluir = tk.Button(root, text="Excluir", command=excluir)
btn_excluir.grid(row=9, column=0, columnspan=2, pady=10)

# Loop principal da janela
root.mainloop()

# Fechamento da conexão com o banco de dados
model.fechar_conexao(conn)
