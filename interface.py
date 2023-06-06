import bancodados

# caminho = str(input('Caminho do banco de dados: '))
# C:\Infopoint\InfoPoint ERP-147\BaseDados\Carloni\INFOPOINTERP.FDB
conn = bancodados.conectar_no_banco()

resultado = bancodados.ler_condicoespgto(conn)
for res in resultado:
    print(res)

bancodados.fechar_conexao(conn)

